init -1500 python:
    class BattleRule(store.object):
        """Represents an action that can be taken by an Actor.
        BattleRule are appended to the Actor.rules attribute to form a list
        of actions in battle.
        """
        def __init__(self,
                     user=None,
                     watches=None,
                     condition=None,
                     action=None,
                     targets=None,
                     target_finder=None,
                     pick_chance=1.0):
            self.user = user
            self.targets = targets
            self.target_finder = target_finder

            self.condition = condition
            if condition is None:
                self.condition = ConditionAlways()

            self.watches = watches

            self.action = action

            self.pick_chance = pick_chance

        @property
        def target_list(self):
            _map = {
                "Self": [self.user],
                "Ally": self.user.allies,
                "Party": self.user.allies + [self.user],
                "Foe": self.user.enemies,
            }
            return _map.get(self.targets)

        @property
        def watcher(self):
            """Always get the latest state of the allies and enemies."""
            watcher_map = {
                "Self": [self.user],
                "Ally": self.user.allies,
                "Party": self.user.allies + [self.user],
                "Foe": self.user.enemies,
            }
            return watcher_map.get(self.watches)

        def __repr__(self):
            return "{}: {}".format(
                self.target_type_name,
                self.action.name
            )

        def roll_chance(self):
            """Roll a random number between 0 and 1. If it's less than the pick_chance,
            the BattleRule is activated.
            """
            pick = random.random()
            if pick <= self.pick_chance:
                return True
            return False

        def act(self):
            """Try to use the BattleRule's action."""
            # If a pick_chance was set, see if the BattleRule will be
            # selected at all.
            result = True
            if self.pick_chance < 1.0:
                result = self.roll_chance()

            if result:
                # Check if the condition has been met
                if not self.condition(self.watcher):
                    return False
                # If something finds a target, call it
                found_targets = self.target_finder(self.target_list)
                return self.action.use(self.user, found_targets)

            return False
