from random import choice, random
# The string with all the possible characters
GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+.\\\"\n"
# Default target string
TARGET = "The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"

class Individual:
    def __init__(self, chromosome = None, target = TARGET):
        self.chromosome = chromosome
        self.fitness = 0
        self.target = target
    
    @staticmethod
    def getRandomGene():
        return choice(GENES) 
    
    @staticmethod
    def getRandomChromosome(target):
        return ''.join(Individual.getRandomGene() for i in range(len(target)))
    
    def calculateFitness(self):
        fit = 0
        for individual, target in zip(self.chromosome, self.target):
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