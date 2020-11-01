from BackpackBruteForce import BackpackBruteForce
from BackpackGeneticAlgorithm import BackpackGeneticAlgorithm
from BackpackGreedyAlgorithm import BackpackGreedyAlgorithm
from ItemsInitilizer import ItemsInitilizer


def cloneItems(ITEMS):
    return list(ITEMS)


def main():
    CAPACITY_SMALL = 25
    CAPACITY_LARGE = 50
    ITEMS_LARGE_COLLECTION_SIZE = 20
    ITEMS_SMALL = ItemsInitilizer.initilizeItems()
    ITEMS_LARGE = ItemsInitilizer.initilizeItemsLarge(ITEMS_LARGE_COLLECTION_SIZE)
    MAX_VALUE_SMALL_CASE = BackpackGreedyAlgorithm.getMaxValue(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    MAX_VALUE_LARGE_CASE = BackpackGreedyAlgorithm.getMaxValue(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)

    print("Small case")
    BackpackBruteForce.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    BackpackGreedyAlgorithm.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    BackpackGeneticAlgorithm.run(ITEMS_SMALL, CAPACITY_SMALL)
    print("\n----------------------------------------------------------------\n")
    print("Large case")
    BackpackBruteForce.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    BackpackGreedyAlgorithm.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    BackpackGeneticAlgorithm.run(ITEMS_LARGE, CAPACITY_LARGE)


if __name__ == "__main__":
    main()
