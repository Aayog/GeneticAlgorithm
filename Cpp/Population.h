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
        /**
         * @brief Construct a new Population object
         * 
         * @param size 
         * @param gene 
         * @param target 
         */
        Population(int size, std::string gene, std::string target);
        /**
         * @brief Initialize the population with the gene, size and
         *        target
         * @param size 
         * @param gene 
         * @param target 
         */
        void initializePopulation(int size, std::string gene, std::string target);
        /**
         * @brief The selection step of the genetic algorithm
         * 
         */
        void selection();
        /**
         * @brief Did the fittest individual reach the target yet?
         * 
         * @return true 
         * @return false 
         */
        bool reachedTarget();
        /**
         * @brief This calculates the fitness for all the 
         *        individuals
         */
        void calculateAllFitness();
        /**
         * @brief Get the Fittest object
         * 
         * @return std::string 
         */
        std::string getFittest();
        /**
         * @brief Get the highest fitness score in a population
         * 
         * @return int 
         */
        int getFittness();
        
        static inline int populationSize = 0;
};
#endif