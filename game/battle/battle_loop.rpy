# Loop for turns in battle
label final_battle:
    show screen battle_scene

    python:
        # Heroes attack
        for hero in enemy_actors:
            if hero.hp > 0:
                hero.turns_used += 1

                for rule in hero.rules:
                    result = rule.act()

                    if result:
                        break
                else:
                    renpy.say(None, "Tried to attack, but could not...")

            if v_actor.hp <= 0:
                renpy.jump("you_lose")

        # Your attack
        v_actor.turns_used += 1
        if v_actor.rules:
            for rule in v_actor.rules:
                result = rule.act()

                if result:
                    break
            else:
                renpy.say(None, "Tried to attack, but could not...")

        if enemy_actors[0].hp <= 0:
            renpy.jump("you_win")

        else:
            renpy.jump("final_battle")
