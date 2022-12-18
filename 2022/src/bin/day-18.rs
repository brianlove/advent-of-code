use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/18-sample.txt";
    // const FILE_NAME: &str = "input/18-sample-basic.txt";
    const FILE_NAME: &str = "input/18-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

fn part1(input: &[String]) -> u32 {
    let cubes = input
        .iter()
        .map(|line| {
            line.split(",")
                .collect::<Vec<_>>()
                .into_iter()
                .map(|s| s.to_string())
                .map(|s| s.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let mut max_dims: [usize; 3] = [0, 0, 0];

    for c in &cubes {
        if c[0] > max_dims[0] {
            max_dims[0] = c[0];
        }
        if c[1] > max_dims[1] {
            max_dims[1] = c[1];
        }
        if c[2] > max_dims[2] {
            max_dims[2] = c[2];
        }
    }

    println!("max dimensions: {max_dims:?}");

    // Examining my input gives max dimensions of [19, 19, 18]
    // These are the max indices, so the actual dimensions are: 20x20x19
    // There's no zero index
    // Also, having an extra buffer at the ends would be good
    // So, let's hard-create our 3D array: 21x21x20

    let mut grid = vec![vec![vec![false; 20]; 21]; 21];
    // let mut grid = vec![vec![vec![false; 8]; 5]; 5];

    for cube in &cubes {
        grid[cube[0]][cube[1]][cube[2]] = true;
    }

    // We want the surface area
    // That happens when a cell that exists meets one that doesn't exist
    // That partitions our cells
    //   - as long as we only count one type , we won't double count edges
    // 

    let mut faces = 0;

    for (x, dim_x) in grid.iter().enumerate() {
        for (y, dim_y) in dim_x.iter().enumerate() {
            for (z, _) in dim_y.iter().enumerate() {
                let cell_faces = check_faces(&grid, (x, y, z));
                faces += cell_faces;
            }
        }
    }

    return faces;
}


/**
 * Check how many air/obsidian boundaries this cell is adjacent to
 */
fn check_faces(grid: &Vec<Vec<Vec<bool>>>, cell: (usize, usize, usize)) -> u32 {
    let mut num_counted = 0;

    // We're only checking cells that exist (i.e. are obsidian)
    if ! grid[cell.0][cell.1][cell.2] {
        return 0;
    }

    if cell.0 == 0 || ! grid[cell.0-1][cell.1][cell.2] {
        num_counted += 1;
        println!("  x-1");
    }
    if ! grid[cell.0+1][cell.1][cell.2] {
        num_counted += 1;
        println!("  x+1");
    }
    if cell.1 == 0 || ! grid[cell.0][cell.1-1][cell.2] {
        num_counted += 1;
        println!("  y-1");
    }
    if ! grid[cell.0][cell.1+1][cell.2] {
        num_counted += 1;
        println!("  y+1");
    }
    if cell.2 == 0 || ! grid[cell.0][cell.1][cell.2-1] {
        num_counted += 1;
        println!("  z-1");
    }
    if ! grid[cell.0][cell.1][cell.2+1] {
        num_counted += 1;
        println!("  z+1");
    }

    return num_counted;
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
