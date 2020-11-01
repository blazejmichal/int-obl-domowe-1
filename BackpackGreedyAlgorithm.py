import timeit

from ItemsInitilizer import ItemsInitilizer


class BackpackGreedyAlgorithm:

    @staticmethod
    def getMaxValue(items, capacity):
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

    @staticmethod
    def run(ITEMS, CAPACITY):
        start = timeit.default_timer()
        maxValue = BackpackGreedyAlgorithm.getMaxValue(ITEMS, CAPACITY)
        stop = timeit.default_timer()
        time = stop - start
        print("Maximum value in Backpack =", maxValue)
        print("Czas dla GreedyAlgorithm: " + str(time))
        return time

# if __name__ == "__main__":
#     capacity = 25
#     ITEMS = ItemsInitilizer.initilizeItems()
#
#     start = timeit.default_timer()
#     maxValue = BackpackGreedyAlgorithm.getMaxValue(ITEMS, capacity)
#     stop = timeit.default_timer()
#     time = stop - start
#     print("Maximum value in Backpack =", maxValue)
#     print("Czas dla GreedyAlgorithm: " + str(time))
