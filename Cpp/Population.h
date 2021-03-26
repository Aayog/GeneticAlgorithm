#include <vector>
#include <iostream>
#include "Individual.h"

#ifndef POPULATION_H
#define POPULATION_H

class Population {
    private:
        std::vector<Individual> population;
        bool isDone;
    public:
        void initializePopulation(int size, std::string gene, std::string target);
        void selection();
        static inline int populationSize = 0;
        bool reachedTarget();
        void calculateAllFitness();
        std::string getFittest();
};
#endif