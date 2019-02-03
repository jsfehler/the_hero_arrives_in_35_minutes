init python:
    from __future__ import division
    import random


    def clamp_overkill(hp, dmg):
        """Don't let attacks send HP into negative numbers."""
        new_dmg = dmg

        projected_result = hp - dmg
        if projected_result < 0:
            overflow = dmg - hp
            new_dmg -= overflow

        return new_dmg


    def calculate_damage(user, target):
        """Calculate the result of user attacking target."""
        power_minus_endurance = (user.weapon.power * random.uniform(1.0, 1.125)) - target.total_endurance
        if power_minus_endurance < 0:
            power_minus_endurance = 1

        attack = int(power_minus_endurance * user.total_strength * (99 + user.total_strength/256))

        attack_plus_mod = int(attack * user.atk_mod_temp)

        final_atk = attack_plus_mod

        # Take into account barriers
        if target.barrier is not None:
            if final_atk >= target.barrier.power:
                target.barrier = None
                renpy.say(None, "{}'s attack broke {}'s barrier!".format(user.name, target.name))
                return 0

            else:
                final_atk -= target.barrier.power

                if final_atk < 0:
                    final_atk = 0

        # Reset temporary attack boost
        user.atk_mod_temp = 1.0

        return final_atk


    @battle_action("Normal Attack")
    def use_normal_attack(user, targets):
        """Basic attack."""
        target = targets[0]
        if target.hp > 0:
            dmg_amount = calculate_damage(user, target)

            final_dmg = clamp_overkill(target.hp, dmg_amount)

            hide_and_show_damage(target.position, final_dmg)

            if user.weapon.name != "Unarmed":
                renpy.say(None, "{} attacks with the {}".format(user.name, user.weapon.name))

            else:
                renpy.say(None, "{} strikes at {}".format(user.name, target.name))

            #renpy.play("audio/sfx/sfx_wpn_laser3.wav", channel="sound")

            target.hp -= final_dmg

        else:
            return False

        return True


    @battle_action("Emperor Kick", cost=20)
    def use_emperor_kick(user, targets):
        """Attacks one target."""
        target = targets[0]
        if target.hp > 0:
            dmg_amount = 1000

            final_dmg = clamp_overkill(target.hp, dmg_amount)

            hide_and_show_damage(target.position, final_dmg)
            #renpy.play("audio/sfx/sfx_wpn_cannon2.wav", channel="sound")

            renpy.say(None, "{} unleashes a powerful kick!".format(user.name, target.name))

            target.hp -= final_dmg

        else:
            return False

        return True


    @battle_action("Fang Kick", cost=50)
    def use_fang_kick(user, targets):
        """Attacks one target."""
        target = targets[0]
        if target.hp > 0:
            dmg_amount = calculate_damage(user, target)

            final_dmg = clamp_overkill(target.hp, dmg_amount)

            hide_and_show_damage(target.position, final_dmg)
            #renpy.play("audio/sfx/sfx_wpn_cannon2.wav", channel="sound")

            renpy.say(None, "Fire erupts from {}'s legs as they charge forward with a devastating kick!".format(user.name, target.name))

            target.hp -= final_dmg

        else:
            return False

        return True


    @battle_action("Aqua Tornado", cost=50)
    def use_aqua_tornado(user, targets):
        """Attacks all targets."""
        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_damage(user, target)

                final_dmg = clamp_overkill(target.hp, dmg_amount)

                hide_and_show_damage(target.position, final_dmg)
                #renpy.play("audio/sfx/sfx_wpn_cannon2.wav", channel="sound")

                renpy.say(None, "A massive whirlpool erupts around {}, engulfing their foes!".format(user.name, target.name))

                target.hp -= final_dmg

            else:
                return False

        return True


    def calculate_spell_damage(spell_power, user, target):
        """Calculate spell power"""
        base = spell_power * random.uniform(1.0, 1.125)
        base = base - target.total_endurance
        base_2 = (2 + user.total_intelligence) * ((50 + user.total_intelligence) / 256)
        base_3 = base * base_2
        attack_plus_mod = int(base_3 * user.atk_mod_temp)

        final_atk = attack_plus_mod

        # Take into account barriers
        if target.barrier is not None:
            if final_atk >= target.barrier.power:
                target.barrier = None
                renpy.say(None, "{}'s attack broke {}'s barrier!".format(user.name, target.name))
                return None

            else:
                final_atk -= target.barrier.power

                if final_atk < 0:
                    final_atk = 0

        # Reset temporary attack boost
        user.atk_mod_temp = 1.0

        return final_atk


    @battle_action("Rising Inferno", cost=30)
    def use_inferno(user, targets):
        """Attack all targets."""
        renpy.say(None, "Jets of magma explode from the ground!")

        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(160, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_wpn_missilelaunch.wav", channel="sound")

                    target.hp -= final_dmg

        return True


    @battle_action("Hyper Blizzard", cost=30)
    def use_blizzard(user, targets):
        """Attack all targets."""
        renpy.say(None, "{} calls upon the power of the storm!".format(user.name))
        renpy.say(None, "A raging blizzard decends upon the battle field!")


        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(130, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_wpn_missilelaunch.wav", channel="sound")

                    target.hp -= final_dmg

        return True


    @battle_action("Vox Plerion", cost=50)
    def use_plerion(user, targets):
        """Attack all targets."""
        renpy.say(None, "{} harnesses the power of the Dark Nebula!".format(user.name))
        renpy.say(None, "Orbs of dark energy strike from every direction!")

        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(210, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_wpn_laser3.wav", channel="sound")

                    target.hp -= final_dmg

        return True


    @battle_action("Geist Firewheel", cost=50)
    def use_firewheel(user, targets):
        """Fire elemental attack."""
        renpy.say(None, "{}'s weapon ignites with roaring flames!".format(user.name))

        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(210, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    renpy.say(None, "{} launches themself into the air and performs a devastating spin attack on {}!".format(user.name, target.name))

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_exp_medium3.wav", channel="sound")


                    target.hp -= final_dmg

        return True


    @battle_action("Knuckle Shotgun", cost=50)
    def use_knuckle_shotgun(user, targets):
        """Physical attack."""
        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(210, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    renpy.say(None, "{} charges forward with a blast of punches!".format(user.name))

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_exp_medium3.wav", channel="sound")


                    target.hp -= final_dmg

        return True


    @battle_action("Solvent Thunder", cost=50)
    def use_solvent_thunder(user, targets):
        """Electrical attack attack."""
        for target in targets:
            if target.hp > 0:
                dmg_amount = calculate_spell_damage(210, user, target)

                if dmg_amount is not None:
                    final_dmg = clamp_overkill(target.hp, dmg_amount)

                    renpy.say(None, "{} attacks with an electrical barrage!".format(user.name))

                    hide_and_show_damage(target.position, final_dmg)
                    #renpy.play("audio/sfx/sfx_exp_medium3.wav", channel="sound")


                    target.hp -= final_dmg

        return True
