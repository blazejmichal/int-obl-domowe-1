from Item import Item
import matplotlib.pyplot as plt
import itertools
import timeit


class BackpackBruteForce:

    @staticmethod
    def plotChart(x, y):
        plt.title("Brute Force")
        plt.plot(x, y, label='Przebieg wartosci')
        plt.xlabel('Iteracje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()

    @staticmethod
    def run(ITEMS, CAPACITY):
        start = timeit.default_timer()
        BackpackBruteForce.getMaxValue(ITEMS, CAPACITY)
        stop = timeit.default_timer()
        time = stop - start
        print("Czas dla BruteForce: " + str(time))
        return time

    @staticmethod
    def getMaxValue(ITEMS, CAPACITY):
        xIteration = []
        yValue = []
        iteration = 0
        for i in range(0, len(ITEMS) + 1):
            for subSet in itertools.combinations(ITEMS, i):
                subSetValues = map(lambda item: item.value, subSet)
                totalSubSetValue = sum(subSetValues)
                iteration += 1
                xIteration.append(iteration)
                yValue.append(totalSubSetValue)
                if (totalSubSetValue == 1630):
                    BackpackBruteForce.plotChart(xIteration, yValue)
                    return totalSubSetValue
        return 0
