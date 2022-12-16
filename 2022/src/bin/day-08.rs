use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/08-sample.txt";
    const FILE_NAME: &str = "input/08-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

#[derive(Debug)]
struct VisibleFrom {
    overall: bool,
    top: bool,
    bottom: bool,
    left: bool,
    right: bool,
}

fn part1(input: &[String]) -> usize {
    let trees = input
        .iter()
        .map(|line| {
            line.chars()
                .map(|ch| ch.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    // println!("trees: {trees:?}");

    let mut visibility: Vec<Vec<VisibleFrom>> = Vec::new();

    let height = trees.len();
    let width = trees[0].len();

    let mut num_visible_interior: usize = 0;

    for (row_ix, row) in trees.iter().enumerate() {
        let mut row_visibility: Vec<VisibleFrom> = Vec::new();

        // Skip the top and bottom rows, since they're all visible
        if row_ix == 0 || row_ix == height - 1 {
            continue;
        }

        for (cell_ix, cell) in row.iter().enumerate() {
            // Skip the left and right columns - they're also all visible
            if cell_ix == 0 || cell_ix == width - 1 {
                continue;
            }

            let mut top = true;
            for y in 0..row_ix {
                if trees[y][cell_ix] >= *cell {
                    top = false;
                }
            }

            let mut bottom = true;
            for y in row_ix+1..height {
                if trees[y][cell_ix] >= *cell {
                    bottom = false;
                }
            }

            let mut left = true;
            for x in 0..cell_ix {
                if row[x] >= *cell {
                    left = false;
                }
            }

            let mut right = true;
            for x in cell_ix+1..width {
                if row[x] >= *cell {
                    right = false;
                }
            }

            let overall = top || bottom || left || right;

            row_visibility.push(VisibleFrom {
                overall,
                top,
                bottom,
                left,
                right,
            });

            if overall {
                num_visible_interior += 1;
            }
        }

        visibility.push(row_visibility);
    }

    // println!("Visibility:\n{visibility:?}");

    let num_visible_exterior = 2*height + 2*width - 4;

    return num_visible_interior + num_visible_exterior;
}


fn part2(input: &[String]) -> u32 {
    let trees = input
        .iter()
        .map(|line| {
            line.chars()
                .map(|ch| ch.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let height = trees.len();
    let width = trees[0].len();

    let mut highest_scenic_score: u32 = 0;

    for (row_ix, row) in trees.iter().enumerate() {
        // Skip the top and bottom rows, since they're all visible
        if row_ix == 0 || row_ix == height - 1 {
            continue;
        }

        for (cell_ix, cell) in row.iter().enumerate() {
            // Skip the left and right columns - they're also all visible
            if cell_ix == 0 || cell_ix == width - 1 {
                continue;
            }

            let mut top = 0;
            for y in (0..row_ix).rev() {
                top += 1;
                if trees[y][cell_ix] >= *cell {
                    break;
                }
            }

            let mut bottom: u32 = 0;
            for y in row_ix+1..height {
                bottom += 1;
                if trees[y][cell_ix] >= *cell {
                    break;
                }
            }

            let mut left: u32 = 0;
            for x in (0..cell_ix).rev() {
                left += 1;
                if row[x] >= *cell {
                    break;
                }
            }

            let mut right: u32 = 0;
            for x in cell_ix+1..width {
                right += 1;
                if row[x] >= *cell {
                    break;
                }
            }

            let score = top * bottom * left * right;
            if score > highest_scenic_score {
                highest_scenic_score = score;
            }
        }
    }

    return highest_scenic_score;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);
    println!("part 1: {}\n", answer1);

    let answer2 = part2(&input);
    println!("part 2: {}\n", answer2);

    return Ok(());
}
