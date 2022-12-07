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
    return 4;
}

fn part2(input: &[String]) -> i32 {
    return 4;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}", answer2);

    return Ok(());
}
