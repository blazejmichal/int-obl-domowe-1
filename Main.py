from BackpackBruteForce import BackpackBruteForce
from BackpackGreedyAlgorithm import BackpackGreedyAlgorithm
from ItemsInitilizer import ItemsInitilizer


def cloneItems(ITEMS):
    return list(ITEMS)


def main():
    ITEMS = ItemsInitilizer.initilizeItems()
    CAPACITY = 25
    BackpackBruteForce.run(cloneItems(ITEMS), CAPACITY)
    BackpackGreedyAlgorithm.run(cloneItems(ITEMS), CAPACITY)


if __name__ == "__main__":
    main()
