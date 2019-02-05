label setup_battle_actors:
    python:
        # Actors for the player
        player_actors = BattleActors()
        player_actors.add_actor(0, v_actor)

        # Opponents to fight in battle
        enemy_actors = BattleActors()

        # Default hero 0 is Warlock Knight
        enemy_actors.add_actor(0, h0_wk)
        enemy_actors.add_actor(1, h1)
        enemy_actors.add_actor(2, h2)
        enemy_actors.add_actor(3, h3)
        enemy_actors.add_enemies([i for i in player_actors])

        player_actors.add_enemies([i for i in enemy_actors])

    return
