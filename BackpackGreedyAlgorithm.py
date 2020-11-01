import timeit
import matplotlib.pyplot as plt


class BackpackGreedyAlgorithm:

    @staticmethod
    def getMaxValue(items, capacity):
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
        BackpackGreedyAlgorithm.plotChart(xIteration, yValue)
        return totalValue

    @staticmethod
    def run(ITEMS, CAPACITY):
        start = timeit.default_timer()
        maxValue = BackpackGreedyAlgorithm.getMaxValue(ITEMS, CAPACITY)
        stop = timeit.default_timer()
        time = stop - start
        print("Max wartosc dla Greedy: " + str(maxValue))
        print("Czas dla GreedyAlgorithm: " + str(time))
        return time

    @staticmethod
    def plotChart(x, y):
        plt.title("Greedy")
        plt.plot(x, y, label='Przebieg wartosci')
        plt.xlabel('Iteracje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()
