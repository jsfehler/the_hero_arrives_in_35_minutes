label setup_hero_0:
    python:
        # Possible actors for hero in position 0

        # Description: Warlock Knight
        h0_wk = Actor(name='Reginald', position=0, battle_sprite="images/battle/heroes/hero_0_wk.png")
        h0_wk.weapon = kingsword_of_the_planet_riders

        # Warlock Knight Ruleset
        h0_wk.rules = [
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(3), action=geist_firewheel, targets="Foe", target_finder=CommandTargetAny()),
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(7), action=focus, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

        # Description: Karate Master
        h0_km = Actor(name='Reginald', position=0, battle_sprite="images/battle/heroes/hero_0_km.png")

        # Karate Master Ruleset
        h0_km.rules = [
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(3), action=knuckle_shotgun, targets="Foe", target_finder=CommandTargetAny()),
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(7), action=hawk_instinct, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

        # Description: Monster Slayer
        h0_ms = Actor(name='Reginald', position=0, battle_sprite="images/battle/heroes/hero_0_ms.png")
        h0_ms.weapon = rosary_of_lamenting_gods

        # Monster Slayer Ruleset
        h0_ms.rules = [
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(3), action=solvent_thunder, targets="Foe", target_finder=CommandTargetAny()),
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(7), action=focus, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

    return


label setup_hero_1:
    python:
        # Mage Gunner
        h1 = Actor(name='Maxwell', position=1, battle_sprite="images/battle/heroes/hero_1.png")
        h1.weapon = the_all_gun_of_the_soul

        # Mage Gunner Ruleset
        # Torch: Increase fire damage dealt to all foes in range.
        # BattleRule("Self", user=h1, targets="Foe", condition=ConditionTurnMultipleOf(3), watches=[h1], action=torch)
        h1.rules = [
            BattleRule(watches="Self", condition=ConditionTargetHPLowerThan(0.3), action=drain, targets="Foe", target_finder=CommandTargetAny()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

    return


label setup_hero_2:
    python:
        # Buffs
        h2 = Actor(name='Helena', position=2, battle_sprite="images/battle/heroes/hero_2.png")
        h2.weapon = bow_of_the_hunter_at_the_end_of_time

        # Buffs Ruleset
        # Bravery: Increase target's strength
        h2.rules = [
            BattleRule(watches="Self", condition=ConditionTurnMultipleOf(5), action=barrier, pick_chance=0.8, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

    return


label setup_hero_3:
    python:
        # Healer
        h3 = Actor(name='Gwen', position=3, battle_sprite="images/battle/heroes/hero_3.png")
        h3.weapon = stave_of_the_cosmic_axis_aligners

        # Healer Ruleset
        h3.rules = [
            BattleRule(watches="Self", condition=ConditionTargetHPLowerThan(0.4), action=curatio, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Self", condition=ConditionTargetHPLowerThan(0.1), action=curatiolux, targets="Self", target_finder=CommandTargetAny()),
            BattleRule(watches="Ally", condition=ConditionTargetHPLowerThan(0.3), action=multicuratio, targets="Party", target_finder=CommandTargetAll()),
            BattleRule(watches="Ally", condition=ConditionTargetHPLowerThan(0.1), action=multicuratiolux, targets="Party", target_finder=CommandTargetAll()),
            BattleRule(watches="Foe", condition=ConditionAlways(), action=normal_attack, targets="Foe", target_finder=CommandTargetAny()),
        ]

    return
