use super::individual::*;
use std::iter::FromIterator;
use rand::Rng;

pub struct Population {
    population: Vec<Individual>,
    is_done: bool,
    population_size: i32,
    target: String
}

impl Population {
    // Constructor for the Population "class"
    pub fn new(size: i32, target: String) -> Population {
        let mut population_vec = Vec::new();
        for _ in 0..size {
            population_vec.push(Individual::random_chromosome(target.clone()));
        }
        Population {
            population: population_vec,
            is_done: false,
            population_size: size,
            target: target
        }
    }
    // performs the selection part of the genetic algorithm
    // sorts a population by decreasing fitness
    // creats children from two random parents with more chances of selection increased by their fitness
    // combines their chromosome with slight mutation and creates a child
    // returns the next generation
    pub fn selection(&mut self) {
        self.population.sort_by(|a, b| b.fitness.partial_cmp(&a.fitness).expect("NaN"));
        let ten_percent = (0.1 * self.population_size as f32) as usize;
        let mut next_gen = Vec::from_iter(self.population[1..ten_percent].iter().cloned());
        if self.population[0].fitness >= 100.0 {
            self.is_done = true;
            return;
        }
        let mut children: Vec<Individual> = Vec::new();
        let size = self.population_size - ten_percent as i32;
        let mut rng = rand::thread_rng();
        for _ in 0..=size {
            let index1 = rng.gen_range(0..size) as usize;
            let index2 = rng.gen_range(0..size) as usize;
            let mut parent1 = self.population[index1].clone();
            let parent2 = &self.population[index2];
            children.push(Individual::new(parent1.mate(parent2)));
        }
        for child in children {
            next_gen.push(child);
        }
        self.population = next_gen;
    }
    
    // check if target is reached
    pub fn reached_target(&self) -> bool {
        self.is_done
    }
    
    // calculates all fitness of the population
    pub fn calculate_all_fitness(&mut self) {
        // self.population.iter().map(|&mut pop| pop.calculate_fitness());
        for individuals in &mut self.population {
            individuals.calculate_fitness();
        }
    }

    // returns printable format of the fittest individual in a population
    // returns the result with fitness score
    pub fn get_fittest(&self) -> String {
        let target = self.target.clone();
        let random_indv = Individual::random_chromosome(target);
        let fittest = match self.population.first() {
            Some(s) => {
                s
            },
            None => &random_indv
        };
        format!("{} : {}", fittest.chromosome, fittest.fitness)
    }
    // making it easier to print
    pub fn print(&self) {
        let pop = &self.population;
        println!("Population is {}", self.is_done);
        println!("Population size is {}", self.population_size);
        for i in pop {
            println!("{}", i.chromosome);
        }
    }
}