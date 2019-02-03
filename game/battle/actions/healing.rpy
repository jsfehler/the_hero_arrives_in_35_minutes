init python:
    from __future__ import division
    import random


    def clamp_overheal(target, restore_amount):
        """Don't let spells send HP above target's max."""
        new_restore = restore_amount

        projected_result = target.hp + int(restore_amount)

        if projected_result > target.total_hp:
            overflow = projected_result - target.total_hp
            new_restore -= overflow

        return new_restore


    def calculate_heal_amount(user, target, factor):
        """Healing uses a standard formula."""
        slice = (target.total_hp * factor)

        restore_amount = slice + (((user.total_intelligence / 3) * slice) / random.uniform(200, 256))

        total = int(clamp_overheal(target, restore_amount))

        return total


    def can_heal_target(target):
        """Checks if target has more than 0 HP.
        """
        if target.hp > 0:
            return True
        return False


    def _heal_target(user, target, base_percentage):
        if target.name == user.name:
            target_name = "their wounds"
        else:
            target_name = user.name

        renpy.say(
            None,
            "{} uses mystical energy to heal {}!".format(
                user.name, target_name)
        )

        r = calculate_heal_amount(user, target, base_percentage)

        hide_and_show_heal(target.position, r)

        #renpy.play("audio/sfx/sfx_sounds_powerup17.wav", channel="sound")

        target.hp += r



    @battle_action("Curatio", cost=10)
    def use_curatio(user, targets):
        """Restore 1/4th the target's HP,
        plus an amount determined by the user's intelligence.
        """
        for target in targets:
            if can_heal_target(target):
                _heal_target(user, target, 0.25)
            else:
                return False

        return True


    @battle_action("Curatiolux", cost=20)
    def use_curatiolux(user, targets):
        """Restore 1/2th the target's HP,
        plus an amount determined by the user's intelligence.
        """
        for target in targets:
            if can_heal_target(target):
                _heal_target(user, target, 0.50)
            else:
                return False

        return True


    @battle_action("Multicuratio", cost=15)
    def use_multicuratio(user, targets):
        """Restore 1/4th the target's HP,
        plus an amount determined by the user's intelligence.
        """
        renpy.say(
            None,
            "{} uses mystical energy to heal the entire party!".format(user.name)
        )

        for target in targets:
            if target.hp > 0:

                r = calculate_heal_amount(user, target, 0.25)

                hide_and_show_heal(target.position, r)

                #renpy.play("audio/sfx/sfx_sounds_powerup17.wav", channel="sound")

                target.hp += r

        return True


    @battle_action("Multicuratiolux", cost=25)
    def use_multicuratiolux(user, targets):
        """Restore 1/4th the target's HP,
        plus an amount determined by the user's intelligence.
        """
        renpy.say(
            None,
            "{} uses mystical energy to heal the entire party!".format(user.name)
        )

        for target in targets:
            if target.hp > 0:
                r = calculate_heal_amount(user, target, 0.50)

                hide_and_show_heal(target.position, r)

                #renpy.play("audio/sfx/sfx_sounds_powerup17.wav", channel="sound")

                target.hp += r

        return True
