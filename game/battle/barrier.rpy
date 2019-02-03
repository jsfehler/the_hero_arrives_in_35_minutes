init -1500 python:
    # TODO: Break formula should probably be in here, not in the actions

    class Barrier(store.object):
        """Barrier that can be added to an Actor.
        Absorbs damage.

        Barrier breaks if attack does at least 2x barrier's power in damage.
        """
        def __init__(self, power):
            self.power = power
