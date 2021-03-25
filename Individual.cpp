#include "Individual.h"
#include <algorithm>
#include <sstream>
#include <iostream>

void Individual::calculateFitness() {
    int fit = 0;
    for (int i = 0; i < this->chromosome.size(); i++) {
        if (this->chromosome[i] == Individual::target[i]){
            fit++;
        }
    }
    this->fitness = ((float) fit / this->chromosome.size()) * 100;
}

std::string Individual::mate(Individual partner) {
    std::stringstream ss;
    std::string XX = this->chromosome, XY = partner.chromosome;
    for (int i = 0; i < this->chromosome.size(); i++) {
        double probability = rand() / double(RAND_MAX);
        if (probability < 0.45) {
            ss << XX[i];
        } else if (probability < 0.90) {
            ss << XY[i];
        } else {
            ss << Individual::getRandomGene();
        }
    }
    return ss.str();
}


char Individual::getRandomGene() {
    int index = rand() % Individual::gene.size();
    return Individual::gene[index];
}

std::string Individual::getRandomChromosome() {
    std::stringstream ss;
    for (int i = 0; i < Individual::target.size(); i++) {
        ss << Individual::getRandomGene();
    }
    return ss.str();
}