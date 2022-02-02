use rand::Rng;
use std::clone::Clone;

pub struct Individual {
    pub chromosome: String,
    pub fitness: f32,
    pub target: String,
}

impl Individual {
    pub fn new(_chromosome: String) -> Individual {
        let target = String::from("to be or not to be");

        Individual {
            chromosome: _chromosome,
            fitness: 0.0,
            target: target
        }
    }
    pub fn calculate_fitness(&mut self) {
        let mut fit = 0.0;
        let chrmsm = &self.chromosome;
        for (i, c) in chrmsm.chars().enumerate() {
            let d = match self.target.chars().nth(i) {
                Some(a) => a,
                None => ' ',
            };
            if c == d {
                fit = fit + 1.0;
            }
        }
        self.fitness = (fit / self.chromosome.len() as f32) * 100.0;
    }

    pub fn mate(&mut self, partner: &Individual) -> String {
        let xx = self.chromosome.to_string();
        let xy = partner.chromosome.to_string();
        let mut rng = rand::thread_rng();
        let mut return_string = String::new();
        for (i, c) in xx.chars().enumerate() {
            let probability = rng.gen_range(0.0..1.0);
            if probability < 0.45 {
                return_string.push(c);
            } else if probability < 0.90 {
                return_string.push(match xy.chars().nth(i) {
                    Some(a) => a,
                    None => ' ',
                });
            } else {
                return_string.push_str(&Individual::random_gene());
            }
        }
        return_string
    }

    pub fn random_chromosome(target: String) -> Individual{
        let mut s = String::new();
        for _ in 0..target.len() {
            s.push_str(&Individual::random_gene());
        }
        Individual {
            chromosome: s,
            target: target,
            fitness: 0.0
        }
    }
    
    pub fn random_gene() -> String{
        let mut rng = rand::thread_rng();
        let genes = String::from("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'()!{}-+.*!");
        let index = rng.gen_range(0..genes.len());
        match genes.chars().nth(index) {
            Some(s) => return String::from(s),
            None => return String::from("")
        }
    }
}
//struct Generate<Individual> (fn() -> Individual);

impl Clone for Individual {
    fn clone(&self) -> Self {
        let chromosome = self.chromosome.clone();
        let target = self.target.clone();
        let fitness = self.fitness;
        Individual {
            chromosome: chromosome,
            fitness: fitness,
            target: target,
        }
    }
}