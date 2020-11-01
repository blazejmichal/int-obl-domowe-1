class Item(object):

    def __init__(self, value=0, weight=0, name=None):
        self.value = value
        self.weight = weight
        self.name = name

    def __lt__(self, other):
        selfCost = self.value // self.weight
        otherCost = other.value // other.weight
        return selfCost < otherCost
