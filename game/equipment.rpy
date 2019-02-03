init -2000 python:

    class Equipment(store.object):
        """Data class for which can be equipped to an Actor to increase
        their stats.
        """
        def __init__(self, name, power=0, defence=0):
            self.name = name
            self.power = power
            self.defence = defence
