// use itertools::Itertools;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/04-sample.txt";
    const FILE_NAME: &str = "input/04-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        // .map(|line| Ok(line?.parse::<i32>()?))
        .collect()
}

fn part1(input: &[String]) -> u32 {
    let mut num_subsets: u32 = 0;

    for line in input {
        println!("{line}");

        let set_0: HashSet<u32>;
        let set_1: HashSet<u32>;

        let split_line = line.split(',').collect::<Vec<_>>();
        let mut range_bounds:Vec<Vec<u32>> = Vec::new();

        for elf_str in split_line {
            println!("  -- {}", elf_str);
            range_bounds.push(
                elf_str
                    .split('-')
                    .collect::<Vec<_>>()
                    .into_iter()
                    .map(|bound| bound.parse::<u32>().unwrap())
                    .collect::<Vec<_>>()
            );
        }

        set_0 = HashSet::from_iter((range_bounds[0][0]..range_bounds[0][1]+1).collect::<Vec<u32>>());
        set_1 = HashSet::from_iter((range_bounds[1][0]..range_bounds[1][1]+1).collect::<Vec<u32>>());

        if set_0.is_subset(&set_1) {
            println!("  > set_0 is subset");
            num_subsets += 1;
        } else if set_1.is_subset(&set_0) {
            println!("  > set_1 is subset");
            num_subsets += 1;
        }
    }
    return num_subsets;
}

fn part2(input: &[String]) -> u32 {
    let mut num_subsets: u32 = 0;

    for line in input {
        // println!("{line}");

        let set_0: HashSet<u32>;
        let set_1: HashSet<u32>;

        let split_line = line.split(',').collect::<Vec<_>>();
        let mut range_bounds:Vec<Vec<u32>> = Vec::new();

        for elf_str in split_line {
            println!("  -- {}", elf_str);
            range_bounds.push(
                elf_str
                    .split('-')
                    .collect::<Vec<_>>()
                    .into_iter()
                    .map(|bound| bound.parse::<u32>().unwrap())
                    .collect::<Vec<_>>()
            );
        }

        set_0 = HashSet::from_iter((range_bounds[0][0]..range_bounds[0][1]+1).collect::<Vec<u32>>());
        set_1 = HashSet::from_iter((range_bounds[1][0]..range_bounds[1][1]+1).collect::<Vec<u32>>());

        let overlap = set_0.intersection(&set_1);
        if overlap.count() > 0 {
            // println!("overlap: {:?} {:?}", set_0, set_1);
            num_subsets += 1;
        }
    }
    return num_subsets;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}", answer2);

    return Ok(());
}
