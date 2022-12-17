use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/10-sample.txt";
    // const FILE_NAME: &str = "input/10-sample-2.txt";
    const FILE_NAME: &str = "input/10-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

fn part1(input: &[String]) -> i32 {
    let mut x: i32 = 1;
    let mut current_instruction: usize = 0;
    let mut cycle: usize = 1;
    let mut signal_totals: i32 = 0;

    while current_instruction < input.len() {
        let split = input[current_instruction].split(" ").collect::<Vec<_>>();

        let mut cycles_per_instr = 1;
        let mut num = 0;
        if split[0] == "addx" {
            cycles_per_instr = 2;
            num = split[1].parse::<i32>().unwrap();
        }

        for c in cycle..(cycle+cycles_per_instr) {
            if c % 40 == 20 {
                let signal_strength = c as i32 * x;
                signal_totals += signal_strength;
                println!("  [{:4}]: signal strength: {:4} * {} = {:5}, total: {:6}", c, c, x, signal_strength, signal_totals);
            }
        }
        cycle += cycles_per_instr;
        x += num;
        current_instruction += 1;
    }

    return signal_totals;
}

fn part2(_input: &[String]) -> i32 {
    return 4;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);
    println!("part 1: {}\n", answer1);

    let answer2 = part2(&input);
    println!("part 2: {}\n", answer2);

    return Ok(());
}
