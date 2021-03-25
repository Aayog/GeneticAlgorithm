#include "Population.h"
#include "Individual.h"
#include <algorithm>
#include <sstream>

void Population::initializePopulation(int size, std::string gene, std::string target) {
    Population::populationSize = size;
    if (Individual::gene == ""){
        Individual::gene = gene;
    }
    if (Individual::target == ""){
        Individual::target = target;
    }
    for (int i = 0; i < Population::populationSize; i++) {
        this->population.push_back(Individual(Individual::getRandomChromosome()));
    }
}

void Population::selection() {
    std::sort(this->population.begin(), this->population.end(),  [](Individual a, Individual b) {
        return a.fitness > b.fitness;
    });
    std::vector<Individual> nextGen;
    // The top 10% make it to the next generation
    for (int i = 0; i < (int) (0.1 * (float) Population::populationSize); i++) {
        nextGen.push_back(this->population[i]);
    }
    if (nextGen[0].fitness >= 100) {
        this->isDone = true;
        return;
    }
    // Time for crossover
    std::vector<Individual> children;
    for (int i = 0; i < (int) (0.9 * (float) Population::populationSize); i++) {
        Individual parent1(Individual::target);
        Individual parent2(Individual::target);
        children.push_back(Individual(parent1.mate(parent2)));
    }
    nextGen.insert(nextGen.end(), children.begin(), children.end());
    this->population = nextGen;
}

bool Population::reachedTarget() {
    return this->isDone;
}

void Population::calculateAllFitness() {
    for (auto &p : this->population) {
        p.calculateFitness();
    }
}
std::string Population::getFittest() {
    std::stringstream ss;
    ss << this->population[0].chromosome;
    ss <<  " : " <<(int)this->population[0].fitness;
    return ss.str();
}
