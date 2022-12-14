// #![allow(unused_imports)]
// #![allow(unused_mut)]
// #![allow(unused_variables)]
// #![allow(dead_code)]

use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/05-sample.txt";
    const FILE_NAME: &str = "input/05-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

// CrateMover 9000 - last year's model!
fn part1(input: &[String]) -> String {
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut config_lines: Vec<String> = Vec::new();
    let mut num_stacks: usize;

    let mut still_in_config = true;

    for line in input {
        if line == "" {
            still_in_config = false;
            let num_config_lines = config_lines.len();


            num_stacks = config_lines[num_config_lines - 2].len();
            println!("Num stacks: {}", num_stacks);

            for _ in 0..num_stacks {
                stacks.push(Vec::new());
            }

            println!("Allocated stacks:\n{:?}\n", stacks); // DEBUG

            // We don't need the last of the config lines (numbering the stacks)
            config_lines.pop();

            for line in config_lines.iter().rev() {
                let mut ix = 0;
                println!("config line: {}", line);
                for ch in line.chars() {
                    if ch != ' ' {
                        stacks[ix].push(ch);
                    }
                    ix += 1;
                }
            }

            println!("Initial config stacks:\n{:?}\n", stacks); // DEBUG
            continue;
        }

        if still_in_config {
            // Record the initial config of the crates

            // Simplify the representation of the initial config
            // We only want letters if there's a crate, or blank space if there isn't
            let replaced = line
                .replace("] [", "")
                .replace("[", "")
                .replace("] ", "")
                .replace("]", "")
                .replace("   ", "");
            config_lines.push(replaced);
        } else {
            // Move the crates

            let instruction: Vec<String> = line.split(" ").map(str::to_string).collect();
            println!("instruction: {:?}", instruction);

            let mut num: usize = 0;
            let mut src: usize = 0;
            let mut dest: usize = 0;
            match instruction[1].parse::<usize>() {
                Ok(val) => num = val,
                Err(_) => (),
            }
            match instruction[3].parse::<usize>() {
                Ok(val) => src = val - 1,
                Err(_) => (),
            }
            match instruction[5].parse::<usize>() {
                Ok(val) => dest = val - 1,
                Err(_) => (),
            }

            for _ in 0..num {
                let this_crate = stacks[src].pop().unwrap();
                println!("    moving {}", this_crate);
                stacks[dest].push(this_crate);
            }

            println!("-- {} --> {},  {}x", src, dest, num);
        }
    }

    let top_of_stacks = stacks.iter().map(|s| *s.last().unwrap()).collect::<Vec<_>>();
    println!("top of stacks: \n{:?}\n", top_of_stacks);

    return top_of_stacks.iter().collect();
}


// CrateMover 9001 - Now capable of moving MULTIPLE crates at once!  (With cupholders!)
fn part2(input: &[String]) -> String {
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut config_lines: Vec<String> = Vec::new();
    let mut num_stacks: usize;

    let mut still_in_config = true;

    for line in input {
        if line == "" {
            still_in_config = false;
            let num_config_lines = config_lines.len();


            num_stacks = config_lines[num_config_lines - 2].len();
            // println!("Num stacks: {}", num_stacks);

            for _ in 0..num_stacks {
                stacks.push(Vec::new());
            }

            // println!("Allocated stacks:\n{:?}\n", stacks); // DEBUG

            // We don't need the last of the config lines (numbering the stacks)
            config_lines.pop();

            for line in config_lines.iter().rev() {
                let mut ix = 0;
                // println!("config line: {}", line);
                for ch in line.chars() {
                    if ch != ' ' {
                        stacks[ix].push(ch);
                    }
                    ix += 1;
                }
            }

            // println!("Initial config stacks:\n{:?}\n", stacks); // DEBUG
            continue;
        }

        if still_in_config {
            // Record the initial config of the crates

            // Simplify the representation of the initial config
            // We only want letters if there's a crate, or blank space if there isn't
            let replaced = line
                .replace("] [", "")
                .replace("[", "")
                .replace("] ", "")
                .replace("]", "")
                .replace("   ", "");
            config_lines.push(replaced);
        } else {
            // Move the crates

            let instruction: Vec<String> = line.split(" ").map(str::to_string).collect();
            // println!("instruction: {:?}", instruction);

            let mut num: usize = 0;
            let mut src: usize = 0;
            let mut dest: usize = 0;
            match instruction[1].parse::<usize>() {
                Ok(val) => num = val,
                Err(_) => (),
            }
            match instruction[3].parse::<usize>() {
                Ok(val) => src = val - 1,
                Err(_) => (),
            }
            match instruction[5].parse::<usize>() {
                Ok(val) => dest = val - 1,
                Err(_) => (),
            }

            let mut crane_crates: Vec<char> = Vec::new();

            for _ in 0..num {
                let this_crate = stacks[src].pop().unwrap();
                crane_crates.push(this_crate);
                // println!("    moving {}", this_crate);
            }

            for _ in 0..num {
                stacks[dest].push(crane_crates.pop().unwrap());
            }

            // println!("-- {} --> {},  {}x", src, dest, num);
        }
    }

    let top_of_stacks = stacks.iter().map(|s| *s.last().unwrap()).collect::<Vec<_>>();
    println!("top of stacks: \n{:?}\n", top_of_stacks);

    return top_of_stacks.iter().collect();
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}\n", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}\n", answer2);

    return Ok(());
}
