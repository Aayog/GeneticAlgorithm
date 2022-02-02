mod pool;
pub use pool::population::*;
pub use pool::individual::*;

fn main() {
    let size = 1000;
    let target = String::from("to be or not to be");

    // let pop = Population::new();.
    println!("{}", target);
    // let mut individual = Individual::new(Individual::random_chromosome(&target), target);
    // individual.calculate_fitness();
    // println!("{}  {}", individual.chromosome, individual.fitness);
    let mut pop = Population::new(size, target);
    // pop.print();
    // let mut i = 0;
    while !pop.reached_target() {
        pop.calculate_all_fitness();
        pop.selection();
        println!("Result: {}%", pop.get_fittest());
        // i += 1;
        // if i > 500 {
        //     break;
        // }
    }
    // pop.print();
}
