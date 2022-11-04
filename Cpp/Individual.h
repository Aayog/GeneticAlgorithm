#include <string>
#include <iostream>
#ifndef INDIVIDUAL_H
#define INDIVIDUAL_H

class Individual {
    private:
        std::string chromosome;
        float fitness;
        friend class Population;
    public:
        Individual(const std::string chromosome = NULL) {
            this->chromosome = chromosome;
        }
        /**
         * @brief Calculates how "fit" the current individual is
         * based on how close it is to the target
         * and assigns a score
         */
        void calculateFitness();
        /**
         * @brief Simulates the mating in an ecosystem where the current
         *        chromosome of the current individual is combined with a
         *        partners genes randomly with 5% mutation 
         * @param partner is another Individual for the mating
         * @return std::string gene of the child
         */
        std::string mate(Individual partner);
        /**
         * @brief Get an individual random Gene object for mutation
         * 
         * @return char: the random single gene char
         */
        static char getRandomGene();
        /**
         * @brief Get the Random Chromosome object for the initialization
         *        of the individual
         * @return std::string of the chromosome
         */
        static std::string getRandomChromosome();
        /**
         * @brief to make sure gene and target can be changed statically
         *        by the population class
         */
        static inline std::string gene = "";
        static inline std::string target = "";
};
#endif