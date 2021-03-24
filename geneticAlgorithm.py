from random import choice, random
import sys

# The string with all the possible characters
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+.\\\""
# Default target string
TARGET = "to be or not to be that is the question"
# Population size, if size is large --> overfitting
POPULATION_SIZE = 1000

# if command line arguments provided use the string as target
if (len(sys.argv) > 1):
    TARGET = sys.argv[1]
    
class Population:
    def __init__(self):
        self.population = []
        self.isDone = False
    
    def initializePopulation(self):
        '''
            Initialize the population with random individuals with random chromosomes
        '''
        self.population = [Individual(Individual.getRandomChromosome()) for _ in range(POPULATION_SIZE)]

    def selection(self):
        '''
            The idea of selection phase is to select the fittest individuals and let them pass their genes to the next generation.
            Two pairs of individuals (parents) are selected based on their fitness scores. 
            Individuals with high fitness have more chance to be selected for reproduction. 
        '''
        self.population = sorted(self.population, key=lambda x:x.fitness, reverse=True)
        nextGeneration = self.population[: int(0.1 * POPULATION_SIZE)] 
        if nextGeneration[0].fitness >= 100:
            self.isDone = True
            return
        children = []
        for _ in range(int(0.9 * POPULATION_SIZE)):
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
        '''
            Crossover is the most significant phase in a genetic algorithm. 
            For each pair of parents to be mated, a crossover point is chosen at random from within the genes.
            Offspring are created by exchanging the genes of parents among themselves until the crossover point is reached.
            
            Mutation
            In certain new offspring formed, some of their genes can be subjected to a mutation with a low random probability. 
            This implies that some of the bits in the bit string can be flipped.
        '''
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
    sys.stdout.write(f"Target: {TARGET}\n")
    pop = Population()
    pop.initializePopulation()
    ct = 0
    while not pop.isDone:
        for p in pop.population:
            p.calculateFitness()
        pop.selection()
        sys.stdout.write(f"\rResult: {pop.population[0]}")
        if ct > 1000000:
            break
        ct += 1


