// use itertools::Itertools;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/01-sample.txt";
    const FILE_NAME: &str = "input/01-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        // .map(|line| Ok(line?.parse::<i32>()?))
        .collect()
}

fn part1(input: &[String]) -> i32 {
    println!("Hello, day 01");

    // let mut elf = 0;
    let mut this_elf_total = 0;
    let mut totals = Vec::new();

    for line in input {
        if line == "" {
            totals.push(this_elf_total);
            // elf += 1;
            this_elf_total = 0;
        } else {
            match line.parse::<i32>() {
                Ok(val) => this_elf_total += val,
                Err(err) => println!("Invalid line! {}", err),
            }
        }
    }
    // Make sure we include the last elf!!
    totals.push(this_elf_total);

    let mut largest_total = 0;

    for total in totals {
        println!("> {}", total);
        if total > largest_total {
            largest_total = total;
        }
    }

    return largest_total;
}

fn part2(input: &[String]) -> i32 {
    let mut this_elf_total = 0;
    let mut totals = Vec::new();

    for line in input {
        if line == "" {
            totals.push(this_elf_total);
            this_elf_total = 0;
        } else {
            match line.parse::<i32>() {
                Ok(val) => this_elf_total += val,
                Err(err) => println!("Invalid line! {}", err),
            }
        }
    }
    // Make sure we include the last elf!!
    totals.push(this_elf_total);

    totals.sort_by(|a, b| b.cmp(a));
    let largest_three = totals[0] + totals[1] + totals[2];

    return largest_three;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}", answer2);

    return Ok(());
}
