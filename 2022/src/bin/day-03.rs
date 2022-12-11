// use itertools::Itertools;
use std::collections::HashSet;
use std::fs::File;
// use std::hash::Hash;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/03-sample.txt";
    const FILE_NAME: &str = "input/03-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        // .map(|line| Ok(line?.parse::<i32>()?))
        .collect()
}

fn char_value(ch: char) -> u32 {
    let raw = ch as u32;
    if raw > 96 {
        return raw - 96;
    } else {
        return raw - 64 + 26;
    }
}

fn part1(input: &[String]) -> u32 {
    let mut total = 0;

    for line in input {
        let midpoint: usize = line.len() / 2;
        let first = &line[..midpoint];
        let second = &line[midpoint..];
        // println!("> {} - {}", first, second);
        let first_set = HashSet::<char>::from_iter(first.chars());
        let second_set = HashSet::<char>::from_iter(second.chars());

        let overlap = first_set.intersection(&second_set);
        for ch in overlap {
            total += char_value(*ch);
        }
    }
    return total;
}

fn part2(input: &[String]) -> u32 {
    let mut total = 0;
    let mut ix = 0;
    let mut charsets: Vec<HashSet<char>> = Vec::new();

    for line in input {
        // println!("{}", line);

        let charset = HashSet::<char>::from_iter(line.chars());
        charsets.push(charset);

        if ix == 2 {
            // We have all three elves in this group

            let mut iter = charsets.iter();
            let base = iter
                .next()
                .unwrap()
                .clone();
            let intersection = iter.fold(base, |acc, set| {
                return acc.intersection(set).map(|x| x.clone()).collect();
            });

            for ch in intersection {
                // println!("  - common: {}", ch);
                total += char_value(ch);
            }

            charsets.clear();
        }

        ix = (ix + 1) % 3;
    }

    return total;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);//.context("Failed to find answer for part 1");
    println!("part 1: {}", answer1);

    let answer2 = part2(&input);//.context("Failed to find answer for part 1");
    println!("part 2: {}", answer2);

    return Ok(());
}
