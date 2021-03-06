from projekt.algorithms.BackpackBruteForce import BackpackBruteForce
from projekt.algorithms.BackpackGeneticAlgorithm import BackpackGeneticAlgorithm
from projekt.algorithms.BackpackGreedyAlgorithm import BackpackGreedyAlgorithm
from projekt.service.ItemsInitilizer import ItemsInitilizer
from matplotlib import pyplot as plt

"""
Uniemozliwa zmiany w inpucie przy przechodzeniu pomiedzy algorytmami.
"""


def cloneItems(ITEMS):
    return list(ITEMS)


"""
Metoda uruchamiajaca projekt
"""


def main():
    CAPACITY_SMALL = 15
    CAPACITY_MEDIUM = 25
    CAPACITY_LARGE = 50
    ITEMS_SMALL_COLLECTION_SIZE = 5
    ITEMS_MEDIUM_COLLECTION_SIZE = 10
    ITEMS_LARGE_COLLECTION_SIZE = 20
    ITEMS_SMALL = ItemsInitilizer.initilizeItemsGivenTimes(ITEMS_SMALL_COLLECTION_SIZE)
    ITEMS_MEDIUM = ItemsInitilizer.initilizeItemsGivenTimes(ITEMS_MEDIUM_COLLECTION_SIZE)
    ITEMS_LARGE = ItemsInitilizer.initilizeItemsGivenTimes(ITEMS_LARGE_COLLECTION_SIZE)
    MAX_VALUE_SMALL_CASE = BackpackGreedyAlgorithm.getMaxValue(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    MAX_VALUE_MEDIUM_CASE = BackpackGreedyAlgorithm.getMaxValue(cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM)
    MAX_VALUE_LARGE_CASE = BackpackGreedyAlgorithm.getMaxValue(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)

    print("Small case")
    # bruteTimeSmall = runBruteForceMultipleTimes(10, cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    # greedyTimeSmall = runGreedyMultipleTimes(10, cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    # geneticTimeSmall = runGeneticForceMultipleTimes(10, cloneItems(ITEMS_SMALL), CAPACITY_SMALL, MAX_VALUE_SMALL_CASE)
    bruteTimeSmall = BackpackBruteForce.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    greedyTimeSmall = BackpackGreedyAlgorithm.run(cloneItems(ITEMS_SMALL), CAPACITY_SMALL)
    geneticTimeSmall = BackpackGeneticAlgorithm.run(ITEMS_SMALL, CAPACITY_SMALL, MAX_VALUE_SMALL_CASE)
    print("\n----------------------------------------------------------------\n")
    print("Medium case")
    # bruteTimeMedium = runBruteForceMultipleTimes(10, cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM)
    # greedyTimeMedium = runGreedyMultipleTimes(10, cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM)
    # geneticTimeMedium = runGeneticForceMultipleTimes(10, cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM,MAX_VALUE_MEDIUM_CASE)
    bruteTimeMedium = BackpackBruteForce.run(cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM)
    greedyTimeMedium = BackpackGreedyAlgorithm.run(cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM)
    geneticTimeMedium = BackpackGeneticAlgorithm.run(cloneItems(ITEMS_MEDIUM), CAPACITY_MEDIUM, MAX_VALUE_MEDIUM_CASE)
    print("\n----------------------------------------------------------------\n")
    print("Large case")
    # bruteTimeLarge = runBruteForceMultipleTimes(10, cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    # greedyTimeLarge = runGreedyMultipleTimes(10, cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    # geneticTimeLarge = runGeneticForceMultipleTimes(10, cloneItems(ITEMS_LARGE), CAPACITY_LARGE, MAX_VALUE_LARGE_CASE)
    bruteTimeLarge = BackpackBruteForce.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    greedyTimeLarge = BackpackGreedyAlgorithm.run(cloneItems(ITEMS_LARGE), CAPACITY_LARGE)
    geneticTimeLarge = BackpackGeneticAlgorithm.run(ITEMS_LARGE, CAPACITY_LARGE, MAX_VALUE_LARGE_CASE)

    plotSummaryChart(bruteTimeSmall, greedyTimeSmall, geneticTimeSmall)
    plotSummaryChart(bruteTimeMedium, greedyTimeMedium, geneticTimeMedium)
    plotSummaryChart(bruteTimeLarge, greedyTimeLarge, geneticTimeLarge)
    print("Koniec")


"""
Metoda wlacza algorytm wieloktornie, w zaleznosci od argumentu i. Umozliwia to obliczenie sredniego czasu z wielu prob.
"""


def runBruteForceMultipleTimes(i, ITEMS, CAPACITY):
    totalValue = 0
    for x in range(i):
        totalValue += BackpackBruteForce.run(ITEMS, CAPACITY)
    return totalValue / i


"""
Metoda wlacza algorytm wieloktornie, w zaleznosci od argumentu i. Umozliwia to obliczenie sredniego czasu z wielu prob.
"""


def runGreedyMultipleTimes(i, ITEMS, CAPACITY):
    totalValue = 0
    for x in range(i):
        totalValue += BackpackGreedyAlgorithm.run(ITEMS, CAPACITY)
    return totalValue / i


"""
Metoda wlacza algorytm wieloktornie, w zaleznosci od argumentu i. Umozliwia to obliczenie sredniego czasu z wielu prob.
"""


def runGeneticForceMultipleTimes(i, ITEMS, CAPACITY, MAX_VALUE):
    totalValue = 0
    for x in range(i):
        totalValue += BackpackGeneticAlgorithm.run(ITEMS, CAPACITY, MAX_VALUE)
    return totalValue / i


"""
Rysuje wykres porownujacy czasy algorytmow w obrebie inputu jednej wielkosci
"""


def plotSummaryChart(bruteTime, greedyTime, geneticTime):
    algorithms = ["Brute Force", "Greedy", "Genetics"]
    times = [bruteTime * 1000, greedyTime * 1000, geneticTime * 1000]
    plt.pie(times, labels=algorithms)
    plt.title("Zestawienie czasow trwania algorytmow")
    plt.show()


"""
Uruchamia skrypt
"""

if __name__ == "__main__":
    main()
