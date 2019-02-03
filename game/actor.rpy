init -2000 python:
    class Curse(store.object):
        """A Curse can boost a single stat, lower a single stat, or do both.

        An Actor can only have one Curse at a time.
        """
        def __init__(self, name, boosted_stat='', lowered_stat=''):
            self.name = name
            self.boosted_stat = boosted_stat
            self.lowered_stat = lowered_stat

            self.boosted_multiplier = 1.1
            self.lowered_multiplier = 0.9

        def calculate(self, name, amount):
            if name == self.boosted_stat:
                return amount * self.boosted_multiplier
            elif name == self.lowered_stat:
                return amount * self.lowered_multiplier
            return amount


    class Actor(store.object):
        """Represents a character in the game."""
        def __init__(self,
                     name,
                     hp=8000,
                     sp=800,
                     strength=10,
                     intelligence=10,
                     endurance=10,
                     perception=10,
                     agility=10,
                     luck=10,
                     position=0,
                     battle_sprite=None):
            self.name = name

            # Story stats
            self.body_size = None
            self.clothing = None
            self.emotion = None

            self.special_form = None
            self.relationship_to_hero = None
            self.mutation = None
            self.sanity = 100

            # Battle stats
            self.hp = hp
            self.sp = sp

            self.total_hp = hp
            self.total_sp = sp

            self.strength = strength
            self.intelligence = intelligence
            self.endurance = endurance
            self.perception = perception
            self.agility = agility
            self.luck = luck

            # Temporary strength increase
            self.strength_mod = 0

            # Equipment
            self.weapon = Equipment('Unarmed', power=11)
            self.helm = Equipment('None', defence=0)
            self.armour = Equipment('None', defence=0)
            self.boots = Equipment('None', defence=0)

            # Battle position
            self.position = position

            # Sprite used in battle
            self.battle_sprite = battle_sprite

            # Counts how many turns are used in battle.
            self.turns_used = 0

            # Temporary multiplier for attacks.
            self.atk_mod_temp = 1.0

            # Damage absorbing barrier.
            self.barrier = None

            # Curse, modifies stats while present
            self.curse = Curse('None')

            # All selectable skills
            self.available_skills = []

            # Private: List of BattleRules for the Actor
            self._rules = []

        @property
        def rules(self):
            return self._rules

        @rules.setter
        def rules(self, new_ruleset):
            for item in new_ruleset:
                item.user = self

            self._rules = new_ruleset

        @property
        def total_strength(self):
            stat_after_curse = self.curse.calculate('strength', self.strength)
            return stat_after_curse

        @property
        def total_intelligence(self):
            stat_after_curse = self.curse.calculate('intelligence', self.intelligence)
            return stat_after_curse

        @property
        def total_endurance(self):
            stat_after_curse = self.curse.calculate('endurance', self.endurance)
            return stat_after_curse + self.armour.defence

        @property
        def total_perception(self):
            stat_after_curse = self.curse.calculate('perception', self.perception)
            return stat_after_curse

        @property
        def total_agility(self):
            stat_after_curse = self.curse.calculate('agility', self.agility)
            return stat_after_curse

        @property
        def total_luck(self):
            stat_after_curse = self.curse.calculate('luck', self.luck)
            return stat_after_curse

        def body_size_plus_clothing(self):
            return '{}:{}'.format(self.body_size, self.clothing)

        def __repr__(self):
            stats = "{} {} {} {} {} {} {}".format(
                self.name,
                self.strength,
                self.intelligence,
                self.endurance,
                self.perception,
                self.agility,
                self.luck
            )
            return stats
