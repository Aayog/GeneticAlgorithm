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
# define POPULATION_SIZE 100
# define MAX 1000000

int main(int argc, char *argv[]) {
    // The string with all the possible characters
    const std::string genes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+.\\\"*!";
    // Default target string
    std::string target = "All the world's a stage, and all the men and women merely players. They have their exits and their entrances;";
    std::cout << target.size() << std::endl;
    if (argc > 1){
        target = argv[1];
    }
    std::cout << "Target: " << target << std::endl;
    // Random seed
    srand (time(NULL));
    
    // Initialized the first generation population
    Population pop(POPULATION_SIZE, genes, target);
    unsigned long count = 0;
    int len = target.size();
    // For every generation until the target is reached
    while (!pop.reachedTarget()) {
        // Get the fitness for all individuals
        pop.calculateAllFitness();
        // Perform the selection process
        pop.selection();
        // Style issues while printing
        if (len <= 120){
            std::cout << "\r";
        }
        // Display the results at the same line
        std::cout << "Result: " << pop.getFittest() <<"%"<< std::flush;;
        if (++count > MAX || pop.getFittness() > 99) {
            break;
        }
    }
    std::cout << std::endl;
}