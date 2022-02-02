from random import choice, random
from Individual import Individual
THRESHOLD = 100
class Population:
    def __init__(self):
        self.population = []
        self.isDone = False
        self.target = None
    
    def initializePopulation(self, size, target):
        '''
            Initialize the population with random individuals with random chromosomes
        '''
        self.population = [Individual(Individual.getRandomChromosome(target)) for _ in range(size)]
        self.target = target

    def selection(self):
        '''
            The idea of selection phase is to select the fittest individuals and let them pass their genes to the next generation.
            Two pairs of individuals (parents) are selected based on their fitness scores. 
            Individuals with high fitness have more chance to be selected for reproduction. 
        '''
        self.population = sorted(self.population, key=lambda x:x.fitness, reverse=True)
        nextGeneration = self.population[: int(0.1 * len(self.population))] 
        if nextGeneration[0].fitness >= THRESHOLD:
            self.isDone = True
            return
        children = []
        for _ in range(int(0.9 * len(self.population))):
            parent1 = choice(nextGeneration)
            parent2 = choice(nextGeneration)
            children.append(Individual(parent1.mate(parent2), self.target))
        self.population = nextGeneration + children

    def __str__(self):
        return '\n'.join(str(p) for p in self.population)

    def __getitem__(self, i):
        return self.population