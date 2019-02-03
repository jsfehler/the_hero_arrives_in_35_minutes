init python:
    from __future__ import division
    import random


    @battle_action('Barrier', cost=10)
    def use_barrier(user, targets):
        """Add barrier that absorbs damage.
        """
        renpy.say(None, "{} creates a barrier!".format(user.name))

        target = targets[0]
        target.barrier = Barrier(int((target.endurance) * (target.endurance / 256) * 25))

        #renpy.play("audio/sfx/sfx_sound_neutral3.wav", channel="sound")

        return True


    @battle_action("Focus", cost=10)
    def use_focus(user, targets):
        """Consume 10% HP to deal 2X damage next turn."""
        renpy.say(None, "{} focuses their energy for the next attack!".format(user.name))

        user.hp -= (user.hp / 10)

        user.atk_mod_temp = 2.0

        #renpy.play("audio/sfx/sfx_sounds_powerup2.wav", channel="sound")

        return True


    @battle_action("Hawk Instinct", cost=10)
    def use_hawk_instinct(user, targets):
        """Increase strength until end of battle."""
        if user.strength_mod < 50:
            renpy.say(None, "{} focues, sending their attack power soaring!".format(user.name))

            user.strength_mod += 10

        else:
            renpy.say(None, "{} focues, but his strength is at maximum!".format(user.name))

            #renpy.play("audio/sfx/sfx_sounds_powerup2.wav", channel="sound")

        return True


    @battle_action('Drain', cost=10)
    def use_drain(user, targets):
        """Drains HP from target, healing for the same amount."""
        target = targets[0]
        renpy.say(None, "{} drains energy from {}!".format(user.name, target.name))

        if target.hp > 0:
            dmg_amount = 1000

            final_dmg = clamp_overkill(target.hp, dmg_amount)

            hide_and_show_damage(target.position, final_dmg)

            #renpy.play("audio/sfx/sfx_sound_nagger2.wav", channel="sound")

            target.hp -= final_dmg
            user.hp += final_dmg
        else:
            return False

        return True
