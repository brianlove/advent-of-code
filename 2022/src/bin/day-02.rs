// use itertools::Itertools;
// use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

const BASE_POINT: i32 = 1;
const LOSS_POINTS: i32 = 0;
const DRAW_POINTS: i32 = 3;
const WIN_POINTS: i32 = 6;


fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/02-sample.txt";
    // const FILE_NAME: &str = "input/02-sample-alt.txt";
    const FILE_NAME: &str = "input/02-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

fn part1(input: &[String]) -> i32 {
    let mut total_points = 0;
    let mut opponent_throw = -1;
    let mut our_throw = -1;

    for line in input {
        let split_line: Vec<&str> = line.split(' ').collect();
        // println!("{} {}", split_line[0], split_line[1]);

        match split_line[0] {
            "A" => opponent_throw = 0, // Rock
            "B" => opponent_throw = 1, // Paper
            "C" => opponent_throw = 2, // Scissors
            &_ => (),
        }
        match split_line[1] {
            "X" => our_throw = 0, // Rock
            "Y" => our_throw = 1, // Paper
            "Z" => our_throw = 2, // Scissors
            &_ => (),
        }

        let our_throw_points = BASE_POINT + our_throw;

        if opponent_throw == our_throw {
            total_points += our_throw_points + DRAW_POINTS;
        } else if (our_throw - opponent_throw + 3) % 3 == 1 {
            total_points += our_throw_points + WIN_POINTS;
        } else {
            total_points += our_throw_points + LOSS_POINTS;
        }
    }

    return total_points;
}

fn part2(input: &[String]) -> i32 {
    let mut total_points = 0;
    let mut opponent_throw = -1;
    let mut end_result = -1;
    let mut end_result_modifier = 0;

    for line in input {
        let split_line: Vec<&str> = line.split(' ').collect();
        // println!("{} {}", split_line[0], split_line[1]);

        match split_line[0] {
            "A" => opponent_throw = 0, // Rock
            "B" => opponent_throw = 1, // Paper
            "C" => opponent_throw = 2, // Scissors
            &_ => (),
        }
        match split_line[1] {
            "X" => {
                end_result = 0;
                end_result_modifier = -1; // Lose
            }
            "Y" => {
                end_result = 3;
                end_result_modifier = 0; // Draw
            }
            "Z" => {
                end_result = 6;
                end_result_modifier = 1; // Win
            }
            &_ => (),
        }

        let our_throw = (opponent_throw + end_result_modifier + 3) % 3;

        let our_throw_points = BASE_POINT + our_throw + end_result;

        total_points += our_throw_points;

        // println!("{}:{}  {}  {}", split_line[0], split_line[1], end_result, (opponent_throw + end_result_modifier + 3) % 3);
    }

    return total_points;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}", answer2);

    return Ok(());
}
