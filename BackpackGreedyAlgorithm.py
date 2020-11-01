import timeit
import matplotlib.pyplot as plt


class BackpackGreedyAlgorithm:

    ITEMS = []
    MAX_VALUE = 0
    CAPACITY = 0

    @classmethod
    def run(cls, ITEMS, CAPACITY, MAX_VALUE):
        cls.setInput(ITEMS, CAPACITY, MAX_VALUE)
        start = timeit.default_timer()
        maxValue = cls.getMaxValue(ITEMS, CAPACITY)
        stop = timeit.default_timer()
        time = stop - start
        print("Max wartosc dla Greedy: " + str(maxValue))
        print("Czas dla GreedyAlgorithm: " + str(time))
        return time

    @classmethod
    def setInput(cls, ITEMS, CAPACITY, MAX_VALUE):
        cls.ITEMS = ITEMS
        cls.CAPACITY = CAPACITY
        cls.MAX_VALUE = MAX_VALUE

    @classmethod
    def getMaxValue(cls, items, capacity):
        items.sort(reverse=True)
        totalValue = 0
        xIteration = []
        yValue = []
        iteration = 0
        for item in items:
            currentWeight = int(item.weight)
            currentValue = int(item.value)
            iteration += 1
            xIteration.append(iteration)
            if capacity - currentWeight >= 0:
                capacity -= currentWeight
                totalValue += currentValue
                yValue.append(totalValue)
            else:
                fraction = capacity / currentWeight
                totalValue += currentValue * fraction
                capacity = int(capacity - (currentWeight * fraction))
                yValue.append(totalValue)
                break
        cls.plotChart(xIteration, yValue)
        return totalValue

    @classmethod
    def plotChart(cls, x, y):
        plt.title("Greedy")
        plt.plot(x, y, label='Przebieg wartosci')
        plt.xlabel('Iteracje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()
