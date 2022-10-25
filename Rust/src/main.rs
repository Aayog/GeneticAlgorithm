mod pool;
pub use pool::population::*;
pub use pool::individual::*;

fn main() {
    let size = 1000;
    let target = String::from("to be or not to be");
    println!("{}", target);
    let mut pop = Population::new(size, target);
    while !pop.reached_target() {
        pop.calculate_all_fitness();
        pop.selection();
        println!("Result: {}%", pop.get_fittest());
    }
}
