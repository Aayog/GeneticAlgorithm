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
        // Individual() {}
        void calculateFitness();
        std::string mate(Individual partner);
        static char getRandomGene();
        static std::string getRandomChromosome();
        static inline std::string gene = "";
        static inline std::string target = "";
};
#endif