init -1500 python:
    # Battle Conditions
    # These represent conditions for a BattleRule being used.
    # When called they must return a boolean.

    class ConditionAlways(object):
        """A condition that will always return True."""
        @property
        def label(self):
            return "Always"

        def __call__(self, targets):
            return True


    class ConditionTurnMultipleOf(object):
        def __init__(self, turn_multiple):
            self.turn_multiple = turn_multiple

        @property
        def label(self):
            return "Turn is multiple of {}".format(self.turn_multiple)

        def __call__(self, targets):
            for target in targets:
                if target.turns_used % self.turn_multiple == 0:
                    return True
            return False


    class ConditionTargetHPLowerThan(object):
        def __init__(self, percentage):
            self.percentage = percentage

        @property
        def label(self):
            percentage_label = str(int(self.percentage * 100))
            return "HP Lower Than {}%".format(percentage_label)

        def __call__(self, targets):
            """HP lower than x. Except if 0."""
            for target in targets:
                if target.hp <= (target.total_hp * self.percentage) and target.hp != 0:
                    return True
            return False


    class ConditionTargetHPGreaterThan(object):
        def __init__(self, percentage):
            self.percentage = percentage

        @property
        def label(self):
            percentage_label = str(int(self.percentage * 100))
            return "HP Greater Than {}%".format(percentage_label)

        def __call__(self, targets):
            """HP greater than x."""
            for target in targets:
                if target.hp >= (target.total_hp * self.percentage):
                    return True
            return False
