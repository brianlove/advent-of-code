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

fn part2(input: &[String]) -> i32 {
    let mut x: i32 = 1;
    let mut current_instruction: usize = 0;
    let mut cycle: usize = 1;

    let mut image: Vec<Vec<char>> = Vec::new();
    let mut row: usize = 0;
    let mut pixel: usize = 0;

    while current_instruction < input.len() {
        let split = input[current_instruction].split(" ").collect::<Vec<_>>();

        let mut cycles_per_instr = 1;
        let mut num = 0;
        if split[0] == "addx" {
            cycles_per_instr = 2;
            num = split[1].parse::<i32>().unwrap();
        }

        for c in cycle..(cycle+cycles_per_instr) {
            if (c - 1) % 40 == 0 {
                pixel = 0;
                row += 1;
                let new_row: Vec<char> = Vec::with_capacity(40);
                image.push(new_row);
            } else {
                pixel += 1;
            }

            if (x-1..x+2).contains(&(pixel as i32)) {
                image[row-1].push('#');
            } else {
                image[row-1].push('.');
            }
        }
        cycle += cycles_per_instr;
        x += num;
        current_instruction += 1;
    }

    println!("Image:");
    for row in image {
        println!("{}", row.into_iter().collect::<String>());
    }

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
