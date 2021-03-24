from random import choice, random
import sys

GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+"
TARGET = "to be or not to be that is the question"
POPULATION_SIZE = 10

if (len(sys.argv) > 1):
    TARGET = sys.argv[1]
    
class Population:
    def __init__(self):
        self.population = []
        self.total_population = 0
        self.isDone = False
    
    def initializePopulation(self):
        self.population = [Individual(Individual.getRandomChromosome()) for _ in range(POPULATION_SIZE)]
        self.total_population = len(self.population)

    def selection(self):
        self.population = sorted(self.population, key=lambda x:x.fitness, reverse=True)
        nextGeneration = self.population[: int(0.1 * self.total_population)] 
        if nextGeneration[0].fitness >= 100:
            self.isDone = True
            return
        children = []
        for _ in range(int(0.9 * self.total_population)):
            parent1 = choice(nextGeneration)
            parent2 = choice(nextGeneration)
            children.append(Individual(parent1.mate(parent2)))
        self.population = nextGeneration + children

    def __str__(self):
        return '\n'.join(str(p) for p in self.population)

    def __getitem__(self, i):
        return self.population

class Individual:
    def __init__(self, chromosome = None):
        self.chromosome = chromosome
        self.fitness = 0
    
    @staticmethod
    def getRandomGene():
        return choice(GENES) 
    
    @staticmethod
    def getRandomChromosome():
        return ''.join(Individual.getRandomGene() for i in range(len(TARGET)))
    
    def calculateFitness(self):
        fit = 0
        for individual, target in zip(self.chromosome, TARGET):
            if individual == target:
                fit += 1
        self.fitness = fit / len(self.chromosome) * 100

    def mate(self, partner):
        child_chromosome = []
        for XX, XY in zip(self.chromosome, partner.chromosome):
            probability = random()
            if probability < 0.45:
                child_chromosome.append(XX)
            elif probability < 0.9:
                child_chromosome.append(XY)
            else:
                child_chromosome.append(Individual.getRandomGene())
        return ''.join(chm for chm in child_chromosome)
    def __str__(self):
        return f'{self.chromosome} : {self.fitness:.0f}%'

if __name__ == "__main__":
    pop = Population()
    pop.initializePopulation()
    ct = 0
    while not pop.isDone:
        for p in pop.population:
            p.calculateFitness()
        pop.selection()
        sys.stdout.write(f"\r{pop.population[0]}")
        if ct > 1000000:
            break
        ct += 1


