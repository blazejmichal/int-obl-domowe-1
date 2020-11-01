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
    def calcualteFitness(cls, chromosome):
        total_value = 0
        total_weight = 0
        index = 0
        for i in chromosome:
            if index >= len(cls.ITEMS):
                break
            if (i == 1):
                total_value += cls.ITEMS[index].value
                total_weight += cls.ITEMS[index].weight
            index += 1

        if total_weight > cls.CAPACITY:
            return 0
        else:
            return total_value

    @classmethod
    def createStartingPopulation(cls, size):
        return [cls.createChromosome() for x in range(0, size)]

    @classmethod
    def createChromosome(cls):
        return [random.randint(0, 1) for x in range(0, len(cls.ITEMS))]

    @classmethod
    def mutateRandomBit(cls, chromosome):
        randomInt = random.randint(0, len(chromosome) - 1)
        if chromosome[randomInt] == 1:
            chromosome[randomInt] = 0
        else:
            chromosome[randomInt] = 1

    @classmethod
    def putBestChromosomesAsFirst(cls, population):
        population = sorted(population, key=lambda chromosome: cls.calcualteFitness(chromosome), reverse=True)
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
            male = parents[random.randint(0, len(parents) - 1)]
            female = parents[random.randint(0, len(parents) - 1)]
            half = len(male) / 2
            child = male[:half] + female[half:]
            child = cls.mutateChromosome(child)
            children.append(child)
        return children

    @classmethod
    def chooseParents(cls, population):
        population = cls.putBestChromosomesAsFirst(population)
        parent_eligibility = 0.2
        parent_length = int(parent_eligibility * len(population))
        parents = population[:parent_length]
        return parents

    @classmethod
    def mutateRandomParents(cls, parents):
        for parent in parents:
            parent = cls.mutateChromosome(parent)
        return parents

    @classmethod
    def mutateChromosome(cls, chromosome):
        mutation_chance = 0.05
        if mutation_chance > random.random():
            cls.mutateRandomBit(chromosome)
        return chromosome

    @classmethod
    def getFitnessValues(cls, population):
        fitnessValues = []
        for chromosome in population:
            fitnessValues.append(cls.calcualteFitness(chromosome))
        return fitnessValues

    @classmethod
    def plotChart(cls, yFitness, yAverage, x):
        plt.plot(x, yFitness, 'r', label='Przebieg wartosci max')
        plt.plot(x, yAverage, 'b', label='Przebieg sredniej')
        plt.xlabel('Generacje')
        plt.ylabel('Wartosci')
        plt.legend()
        plt.show()

    @classmethod
    def run(cls, ITEMS, CAPACITY):
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
        cls.plotChart(yMax, yAverage, xGenerations)

        stop = timeit.default_timer()
        time = stop - start
        print("Czas dla GeneticAlgorithm: " + str(time))
        return time

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
    def setInput(cls, ITEMS, CAPACITY):
        cls.ITEMS = ITEMS
        cls.CAPACITY = CAPACITY
