# Style for damage display
style damage_text:
    size 42
    color "#ff00ff"


# Style for heal display
style heal_text:
    size 42
    color "#00ff00"


# Displays the heroes at the start of battle
transform enemy_appear(x):
    xpos x
    ypos 0.10
    alpha 0.0
    xzoom 0.0
    yzoom 0.0

    parallel:
        easein 1.0 alpha 1.0
    parallel:
        linear 0.5 xzoom 1.0
    parallel:
        linear 0.5 yzoom 1.0
    parallel:
        easeout 0.5 ypos 0.15


# Animates the damage display
# Moves a display from (start_x, start_y) up 25 pixels
transform hit_amount(start_x, start_y):
    xpos start_x
    ypos start_y
    alpha 1.0

    linear 0.2 ypos start_y - 25
    linear 0.8 alpha 0.0


init python:
    # The [x, y] location for each battle sprite
    damage_target_mapping = {
        0: [0.15, 300],
        1: [0.35, 300],
        2: [0.55, 300],
        3: [0.75, 300],
        4: [0.50, 550], # Villain
    }

# Shows a number in front of a character. Used for damage and healing display
screen battle_number_display(target_number, amount, text_style="default"):
    text str(amount) at hit_amount(damage_target_mapping[target_number][0], damage_target_mapping[target_number][1]) style text_style


# Show Name and HP for a single Actor
screen battle_ui(actor):
    vbox:
        ypos 10
        hbox:
            text "{}".format(actor.name)
            # Icons for status effects
            if actor.barrier is not None:
                add "images/battle/icons/barrier.png"
        hbox:
            xsize 300
            text "HP: "
            bar value int(actor.hp) range int(actor.total_hp)


# Screen to display the battle
screen battle_scene():
    # Adds Opponent Health Bars
    hbox:
        xpos 10
        spacing 20
        use battle_ui(enemy_actors[0])
        use battle_ui(enemy_actors[1])
        use battle_ui(enemy_actors[2])
        use battle_ui(enemy_actors[3])

    # Adds Opponent Sprites
    for i, actor in enumerate(enemy_actors):
        add actor.battle_sprite at enemy_appear(damage_target_mapping[i][0])

    # Villain Health Bar
    frame:
        background None
        xalign 0.5
        yalign 0.6
        use battle_ui(v_actor)
