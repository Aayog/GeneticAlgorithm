/**
 * A program to use multiple threads to spell check words from a given 
 * text file.
 * File:   GeneticAlgorithm.cpp
 * Author: Aayog Koirala
 * Copyright (C) 2021 1aayogkoirala@gmail.com
 */

#include <iostream>
#include <time.h>
#include <vector>
#include "Population.h"
#include "Individual.h"

// Population size, if size is large --> overfitting
# define POPULATION_SIZE 1000
# define MAX 1000000
int main(int argc, char *argv[]) {
    // The string with all the possible characters
    const std::string genes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+.\\\"";
    // Default target string
    std::string target = "Crossover is the most significant phase in a genetic algorithm. For each pair of parents to be mated, a crossover point is chosen at random from within the genes. Offspring are created by exchanging the genes of parents among themselves until the crossover point is reached.";
    if (argc > 1){
        target = argv[1];
    }
    
    std::cout << "Target: " << target << std::endl;
    
    srand (time(NULL));
    Population pop;
    pop.initializePopulation(POPULATION_SIZE, genes, target);
    unsigned long count = 0;
    while (!pop.reachedTarget()) {
        pop.calculateAllFitness();
        pop.selection();
        // pop.print();
        std::cout << "\rResult: " << pop.getFittest() <<"%"<< std::flush;;
        if (++count > MAX) {
            break;
        }
    }
}