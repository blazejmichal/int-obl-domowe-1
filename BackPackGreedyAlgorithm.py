# Python3 program to solve fractional
# Knapsack Problem
from Item import Item


# class ItemValue:
#     """Item Value DataClass"""
#
#     def __init__(self, wt, val, ind):
#         self.wt = wt
#         self.val = val
#         self.ind = ind
#         self.cost = val // wt
#
#     def __lt__(self, other):
#         return self.cost < other.cost


# Greedy Approach


class FractionalKnapSack:

    @staticmethod
    def initilizeItems():
        ITEMS = [Item() for i in range(11)]
        ITEMS[0] = Item(100, 7, "zegar")
        ITEMS[1] = Item(300, 7, "obraz-pejzaz")
        ITEMS[2] = Item(200, 6, "obraz-portret")
        ITEMS[3] = Item(40, 2, "radio")
        ITEMS[4] = Item(500, 5, "laptop")
        ITEMS[5] = Item(70, 6, "lampka nocna")
        ITEMS[6] = Item(100, 1, "srebrne sztucce")
        ITEMS[7] = Item(250, 3, "porcelana")
        ITEMS[8] = Item(300, 10, "figura z brazu")
        ITEMS[9] = Item(280, 3, "skorzana torebka")
        ITEMS[10] = Item(300, 15, "odkurzacz")
        return ITEMS

    """Time Complexity O(n log n)"""

    @staticmethod
    def getMaxValue(items, capacity):
        """function to get maximum value """
        # iVal = []
        # for i in range(len(wt)):
        #     iVal.append(ItemValue(wt[i], val[i], i))

        # sorting items by value
        # items = sorted(items, key=lambda cos: cos.value, reverse=True)
        # items.sort(Item.compareItems)
        items.sort(reverse=True)
        totalValue = 0
        for item in items:
            currentWeight = int(item.weight)
            currentValue = int(item.value)
            if capacity - currentWeight >= 0:
                capacity -= currentWeight
                totalValue += currentValue
            else:
                fraction = capacity / currentWeight
                totalValue += currentValue * fraction
                capacity = int(capacity - (currentWeight * fraction))
                break
        return totalValue


# Driver Code
if __name__ == "__main__":
    capacity = 25
    ITEMS = FractionalKnapSack.initilizeItems()

    maxValue = FractionalKnapSack.getMaxValue(ITEMS, capacity)
    print("Maximum value in Knapsack =", maxValue)

# This code is contributed by vibhu4agarwal
