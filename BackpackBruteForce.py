import matplotlib.pyplot as plt
import itertools
import timeit


class BackpackBruteForce:
    ITEMS = []
    MAX_VALUE = 0
    CAPACITY = 0

    @classmethod
    def run(cls, ITEMS, CAPACITY, MAX_VALUE):
        cls.setInput(ITEMS, CAPACITY, MAX_VALUE)
        start = timeit.default_timer()
        bestSet = cls.getBestSet(ITEMS, CAPACITY)
        stop = timeit.default_timer()
        time = stop - start
        cls.printInfo(time, bestSet)
        return time

    @classmethod
    def setInput(cls, ITEMS, CAPACITY, MAX_VALUE):
        cls.ITEMS = ITEMS
        cls.CAPACITY = CAPACITY
        cls.MAX_VALUE = MAX_VALUE

    @classmethod
    def getBestSet(cls, ITEMS, CAPACITY):
        xIteration = []
        yValue = []
        iteration = 0
        matchingSets = []
        for i in range(0, len(ITEMS) + 1):
            for subSet in itertools.combinations(ITEMS, i):
                subSetValue = cls.getSetValue(subSet)
                subSetWeights = map(lambda item: item.weight, subSet)
                subSetWeight = sum(subSetWeights)
                iteration += 1
                if (subSetWeight <= CAPACITY):
                    xIteration.append(iteration)
                    yValue.append(subSetValue)
                    matchingSets.append(subSet)
        cls.plotChart(xIteration, yValue)
        return max(matchingSets, key=lambda matchingSet: cls.getSetValue(matchingSet))

    @classmethod
    def plotChart(cls, x, y):
        plt.title("Brute Force")
        plt.plot(x, y, label='Przebieg wartosci')
        plt.xlabel('Iteracje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()

    @classmethod
    def getSetValue(cls, set):
        setValues = map(lambda item: item.value, set)
        return sum(setValues)

    @classmethod
    def printInfo(cls, time, bestSet):
        print("\n")
        print("Algorytm Brute Force")
        print("Czas: " + str(time))
        print("Znaleziony zestaw: " + str(bestSet))
        print("\n")
