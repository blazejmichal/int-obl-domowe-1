import random
from zadania.item import Item
import numpy as numpy
import matplotlib.pyplot as plt

ITEMS = [Item() for i in range(11)]
CAPACITY = 25
POPULATION_SIZE = 200
GENERATION_AMOUNT = 100


def initilizeItems():
    ITEMS[0] = Item(100, 7, "zegar")
    ITEMS[1] = Item(300, 7, "obraz-pejzaz")
    ITEMS[2] = Item(200, 6, "obraz-portret")
    ITEMS[3] = Item(40, 2, "radio")
    ITEMS[4] = Item(500, 5, "laptop")
    ITEMS[5] = Item(70, 6, "lampka nocna")
    ITEMS[6] = Item(100, 1, "srebrne sztucce")
    ITEMS[7] = Item(250, 3, "porcelana")
    ITEMS[8] = Item(300, 10, "figura z brazu")
    ITEMS[9] = Item(280, 3, "skorzana torebka")
    ITEMS[10] = Item(300, 15, "odkurzacz")


def calcualteFitness(chromosome):
    total_value = 0
    total_weight = 0
    index = 0
    for i in chromosome:
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1

    if total_weight > CAPACITY:
        return 0
    else:
        return total_value


def createStartingPopulation(size):
    return [createChromosome() for x in range(0, size)]


def createChromosome():
    return [random.randint(0, 1) for x in range(0, len(ITEMS))]


def mutateRandomBit(chromosome):
    randomInt = random.randint(0, len(chromosome) - 1)
    if chromosome[randomInt] == 1:
        chromosome[randomInt] = 0
    else:
        chromosome[randomInt] = 1


def putBestChromosomesAsFirst(population):
    population = sorted(population, key=lambda chromosome: calcualteFitness(chromosome), reverse=True)
    return population


def evolvePopulation(population):
    parents = chooseParents(population)
    parents = mutateRandomParents(parents)
    children = createChildren(parents)
    parents.extend(children)
    return parents


def createChildren(parents):
    children = []
    desired_length = POPULATION_SIZE - len(parents)
    while len(children) < desired_length:
        male = parents[random.randint(0, len(parents) - 1)]
        female = parents[random.randint(0, len(parents) - 1)]
        half = len(male) / 2
        child = male[:half] + female[half:]
        child = mutateChromosome(child)
        children.append(child)
    return children


def chooseParents(population):
    population = putBestChromosomesAsFirst(population)
    parent_eligibility = 0.2
    parent_length = int(parent_eligibility * len(population))
    parents = population[:parent_length]
    return parents


def mutateRandomParents(parents):
    for parent in parents:
        parent = mutateChromosome(parent)
    return parents


def mutateChromosome(chromosome):
    mutation_chance = 0.05
    if mutation_chance > random.random():
        mutateRandomBit(chromosome)
    return chromosome


def getFitnessValues(population):
    fitnessValues = []
    for chromosome in population:
        fitnessValues.append(calcualteFitness(chromosome))
    return fitnessValues


def plotChart(yFitness, yAverage, x):
    plt.plot(x, yFitness, 'r', label='Przebieg wartosci max')
    plt.plot(x, yAverage, 'b', label='Przebieg sredniej')
    plt.xlabel('Generacje')
    plt.ylabel('Wartosci')
    plt.legend()
    plt.show()


def main():
    yMax = []
    yAverage = []
    xGenerations = []
    initilizeItems()
    generation = 1
    population = createStartingPopulation(POPULATION_SIZE)
    for i in range(0, GENERATION_AMOUNT):
        print "Generation " + str(generation) + " with " + str(len(population))
        # population = sorted(population, key=lambda x: calcualteFitness(x), reverse=True)
        for j in population:
            print str(j) + ", fit: " + str(calcualteFitness(j))
        fitnessValues = getFitnessValues(population)
        updateX(xGenerations, generation)
        updateYMax(yMax, fitnessValues)
        updateYAverage(yAverage, fitnessValues)
        population = evolvePopulation(population)
        generation += 1
    plotChart(yMax, yAverage, xGenerations)


def updateX(xGenerations, generation):
    xGenerations.append(generation)


def updateYMax(yMax, fitnessValues):
    maxFitness = numpy.max(fitnessValues)
    yMax.append(maxFitness)


def updateYAverage(yAverage, fitnessValues):
    averageFitness = numpy.average(fitnessValues)
    yAverage.append(averageFitness)


if __name__ == "__main__":
    main()
