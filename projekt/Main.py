from projekt.algorithms.BackpackBruteForce import BackpackBruteForce
from projekt.algorithms.BackpackGeneticAlgorithm import BackpackGeneticAlgorithm
from projekt.algorithms.BackpackGreedyAlgorithm import BackpackGreedyAlgorithm
from projekt.service.ItemsInitilizer import ItemsInitilizer
from matplotlib import pyplot as plt


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
    bruteTimeSmall = BackpackBruteForce.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    greedyTimeSmall = BackpackGreedyAlgorithm.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    geneticTimeSmall = BackpackGeneticAlgorithm.run(ITEMS_SMALL, CAPACITY_SMALL, MAX_VALUE_SMALL_CASE)
    print("\n----------------------------------------------------------------\n")
    print("Large case")
    bruteTimeLarge = BackpackBruteForce.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    greedyTimeLarge = BackpackGreedyAlgorithm.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    geneticTimeLarge = BackpackGeneticAlgorithm.run(ITEMS_LARGE, CAPACITY_LARGE, MAX_VALUE_LARGE_CASE)

    plotSummaryChartSmallCase(bruteTimeSmall, greedyTimeSmall, geneticTimeSmall)
    plotSummaryChartLargeCase(bruteTimeLarge, greedyTimeLarge, geneticTimeLarge)


def plotSummaryChartSmallCase(bruteTimeSmall, greedyTimeSmall, geneticTimeSmall):
    algorithms = ["Brute Force", "Greedy", "Genetics"]
    times = [bruteTimeSmall * 1000, greedyTimeSmall * 1000, geneticTimeSmall * 1000]
    plt.pie(times, labels=algorithms)
    plt.title("Malo danych wejsciowych")
    plt.show()


def plotSummaryChartLargeCase(bruteTimeLarge, greedyTimeLarge,geneticTimeLarge):
    algorithms = ["Brute Force", "Greedy", "Genetics"]
    times = [bruteTimeLarge * 1000, greedyTimeLarge * 1000, geneticTimeLarge * 1000]
    plt.pie(times, labels=algorithms)
    plt.title("Duzo danych wejsciowych")
    plt.show()


if __name__ == "__main__":
    main()
