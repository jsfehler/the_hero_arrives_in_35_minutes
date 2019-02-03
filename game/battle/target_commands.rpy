init -1500 python:
    # Target Commands
    # Decides who is hit by a skill

    class CommandTargetLowestHP(object):
        label = "Highest HP"
        description = "Return the target with the highest HP."
        def __call__(self, targets):
            lowest = targets[0]
            for target in targets:
                if target.hp < lowest.hp:
                    lowest = target

            return [lowest]


    class CommandTargetHighestHP(object):
        label = "Highest HP"
        description = "Return the target with the highest HP."
        def __call__(self, targets):
            highest = targets[0]
            for target in targets:
                if target.hp > highest.hp:
                    highest = target

            return [highest]


    class CommandTargetLowestEndurance(object):
        label = "Lowest Endurance"
        description = "Return the target with the lowest total endurance. Ignores KO'd targets."
        def __call__(self, targets):
            lowest = targets[0]
            for target in targets:
                if target.total_endurance < lowest.total_endurance and target.hp != 0:
                    lowest = target

            return [lowest]


    class CommandTargetAll(object):
        label = "All"
        description = "Return all targets."
        def __call__(self, targets):
            return targets


    class CommandTargetAny(object):
        label = "Any"
        description = "Pick one random target"
        def __call__(self, targets):
            # Automatically select a random target
            no_pick_yet = True

            # Don't pick KO'd targets
            while no_pick_yet:
                target_number = random.randint(0, len(targets) - 1)
                target = targets[target_number]
                if target.hp > 0:
                    no_pick_yet = False

            return [target]
