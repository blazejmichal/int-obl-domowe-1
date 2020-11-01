import random
import timeit
import numpy as numpy
import matplotlib.pyplot as plt


class BackpackGeneticAlgorithm:
    ITEMS = []
    MAX_VALUE = 0
    CAPACITY = 0
    POPULATION_SIZE = 200
    GENERATION_AMOUNT = 100

    @classmethod
    def run(cls, ITEMS, CAPACITY, MAX_VALUE):
        yMax = []
        yAverage = []
        xGenerations = []
        cls.setInput(ITEMS, CAPACITY)
        start = timeit.default_timer()
        generation = 0
        population = cls.createStartingPopulation(cls.POPULATION_SIZE)
        for i in range(0, cls.GENERATION_AMOUNT):
            fitnessValues = cls.getFitnessValues(population)
            cls.updateX(xGenerations, generation)
            cls.updateYMax(yMax, fitnessValues)
            cls.updateYAverage(yAverage, fitnessValues)
            population = cls.evolvePopulation(population)
            generation += 1
            if MAX_VALUE in fitnessValues:
                break
        stop = timeit.default_timer()
        time = stop - start
        cls.plotChart(yMax, yAverage, xGenerations)
        cls.printInfo(time)
        return time

    @classmethod
    def setInput(cls, ITEMS, CAPACITY):
        cls.ITEMS = ITEMS
        cls.CAPACITY = CAPACITY

    @classmethod
    def createStartingPopulation(cls, size):
        return [cls.createChromosome() for i in range(0, size)]

    @classmethod
    def getFitnessValues(cls, population):
        fitnessValues = []
        for chromosome in population:
            fitnessValues.append(cls.calculateFitness(chromosome))
        return fitnessValues

    @classmethod
    def calculateFitness(cls, chromosome):
        totalValue = 0
        totalWeight = 0
        index = 0
        for i in chromosome:
            if index >= len(cls.ITEMS):
                break
            if (i == 1):
                totalValue += cls.ITEMS[index].value
                totalWeight += cls.ITEMS[index].weight
            index += 1

        if totalWeight > cls.CAPACITY:
            return 0
        else:
            return totalValue

    @classmethod
    def createChromosome(cls):
        return [random.randint(0, 1) for i in range(0, len(cls.ITEMS))]

    @classmethod
    def mutateRandomBit(cls, chromosome):
        randomInt = random.randint(0, len(chromosome) - 1)
        if chromosome[randomInt] == 1:
            chromosome[randomInt] = 0
        else:
            chromosome[randomInt] = 1

    @classmethod
    def putBestChromosomesAsFirst(cls, population):
        population = sorted(population, key=lambda chromosome: cls.calculateFitness(chromosome), reverse=True)
        return population

    @classmethod
    def evolvePopulation(cls, population):
        parents = cls.chooseParents(population)
        parents = cls.mutateRandomParents(parents)
        children = cls.createChildren(parents)
        parents.extend(children)
        return parents

    @classmethod
    def createChildren(cls, parents):
        children = []
        desired_length = cls.POPULATION_SIZE - len(parents)
        while len(children) < desired_length:
            parent0 = parents[random.randint(0, len(parents) - 1)]
            parent1 = parents[random.randint(0, len(parents) - 1)]
            half = len(parent0) / 2
            child = parent0[:half] + parent1[half:]
            child = cls.mutateChromosome(child)
            children.append(child)
        return children

    @classmethod
    def chooseParents(cls, population):
        population = cls.putBestChromosomesAsFirst(population)
        parentEligibility = 0.3
        parentLength = int(parentEligibility * len(population))
        parents = population[:parentLength]
        return parents

    @classmethod
    def mutateRandomParents(cls, parents):
        for parent in parents:
            parent = cls.mutateChromosome(parent)
        return parents

    @classmethod
    def mutateChromosome(cls, chromosome):
        mutationChance = 0.10
        if mutationChance > random.random():
            cls.mutateRandomBit(chromosome)
        return chromosome

    @classmethod
    def plotChart(cls, yFitness, yAverage, x):
        plt.plot(x, yFitness, 'r', label='Przebieg wartosci max')
        plt.plot(x, yAverage, 'b', label='Przebieg sredniej')
        plt.xlabel('Generacje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()

    @classmethod
    def updateX(cls, xGenerations, generation):
        xGenerations.append(generation)

    @classmethod
    def updateYMax(cls, yMax, fitnessValues):
        maxFitness = numpy.max(fitnessValues)
        yMax.append(maxFitness)

    @classmethod
    def updateYAverage(cls, yAverage, fitnessValues):
        averageFitness = numpy.average(fitnessValues)
        yAverage.append(averageFitness)

    @classmethod
    def printInfo(cls, time):
        print("\n")
        print("Algorytm Genetic")
        print("Czas: " + str(time))
        print("\n")
