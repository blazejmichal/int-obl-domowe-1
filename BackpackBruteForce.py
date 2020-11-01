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
        bestSet = BackpackBruteForce.getBestSet(ITEMS, CAPACITY)
        maxValue = BackpackBruteForce.getSetValue(bestSet)
        stop = timeit.default_timer()
        time = stop - start
        print("Czas dla BruteForce: " + str(time))
        print("Max wartosc dla BruteForce: " + str(maxValue))
        return time

    @staticmethod
    def getBestSet(ITEMS, CAPACITY):
        xIteration = []
        yValue = []
        iteration = 0
        matchingSets = []
        for i in range(0, len(ITEMS) + 1):
            for subSet in itertools.combinations(ITEMS, i):
                subSetValue = BackpackBruteForce.getSetValue(subSet)
                subSetWeights = map(lambda item: item.weight, subSet)
                subSetWeight = sum(subSetWeights)
                iteration += 1
                if (subSetWeight <= CAPACITY):
                    xIteration.append(iteration)
                    yValue.append(subSetValue)
                    matchingSets.append(subSet)
        BackpackBruteForce.plotChart(xIteration, yValue)
        return max(matchingSets, key=lambda matchingSet: BackpackBruteForce.getSetValue(matchingSet))

    @staticmethod
    def getSetValue(set):
        setValues = map(lambda item: item.value, set)
        return sum(setValues)
