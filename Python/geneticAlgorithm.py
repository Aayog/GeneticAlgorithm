import sys
from Population import Population
from Individual import Individual

# Default target string
TARGET = "The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"
# Population size, if size is large --> overfitting
POPULATION_SIZE = 1000
# if command line arguments provided use the string as target
if (len(sys.argv) > 1):
    TARGET = sys.argv[1]

def main():
    sys.stdout.write(f"Target: {TARGET}\n")
    # Population.TARGET = TARGET
    # Population.POPULATION_SIZE = POPULATION_SIZE
    pop = Population()
    pop.initializePopulation(POPULATION_SIZE, TARGET)
    ct = 0
    while not pop.isDone:
        for p in pop.population:
            p.calculateFitness()
        pop.selection()
        sys.stdout.write(f"\rResult: {pop.population[0]}")
        if ct > 1000000:
            break
        ct += 1

if __name__ == "__main__":
    main()
