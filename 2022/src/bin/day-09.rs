use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/09-sample.txt";
    // const FILE_NAME: &str = "input/09-sample-2.txt";
    const FILE_NAME: &str = "input/09-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

fn part1(input: &[String]) -> usize {
    let mut visited_spaces: HashSet<(i32, i32)> = HashSet::from([(0, 0)]);
    let mut head = (0, 0);
    let mut tail = (0, 0);

    for line in input {
        let split = line.split(" ").collect::<Vec<_>>();
        let dir = split[0];
        let num = split[1].parse::<u32>().unwrap();

        for _round in 0..num {
            // Move the head
            if dir == "U" {
                head.1 += 1;
            } else if dir == "D" {
                head.1 -= 1;
            } else if dir == "L" {
                head.0 -= 1;
            } else if dir == "R" {
                head.0 += 1;
            }

            if head.0 == tail.0 {
                if head.1 - tail.1 == 2 {
                    tail.1 += 1;
                } else if tail.1 - head.1 == 2 {
                    tail.1 -= 1;
                }
            } else if head.1 == tail.1 {
                if head.0 - tail.0 == 2 {
                    tail.0 += 1;
                } else if tail.0 - head.0 == 2 {
                    tail.0 -= 1;
                }
            } else {
                // Diagonals...
                let delta = (head.0 - tail.0, head.1 - tail.1);
                // println!("line: {line}");
                // println!("  string: H{head:?} T{tail:?}");
                // println!("  delta: {delta:?}");

                if delta.0 == 1 && delta.1 == 1 {
                    continue;
                } else if delta.0 == 2 || delta.0 == -2 || delta.1 == 2 || delta.1 == -2 {
                    if delta.0 > 0 {
                        tail.0 += 1;
                    } else {
                        tail.0 -= 1;
                    }

                    if delta.1 > 0 {
                        tail.1 += 1;
                    } else {
                        tail.1 -= 1;
                    }
                }
            }

            visited_spaces.insert(tail);
        }
    }

    // println!("Visited spaces: {visited_spaces:?}");
    return visited_spaces.len();
}

fn part2(input: &[String]) -> usize {
    let mut visited_spaces: HashSet<(i32, i32)> = HashSet::from([(0, 0)]);

    // let mut rope: Vec<(i32, i32)> = Vec::new();

    let mut rope = [
        (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    ];

    for line in input {
        let split = line.split(" ").collect::<Vec<_>>();
        let dir = split[0];
        let num = split[1].parse::<u32>().unwrap();

        for _round in 0..num {
            // Move the head
            if dir == "U" {
                rope[0].1 += 1;
            } else if dir == "D" {
                rope[0].1 -= 1;
            } else if dir == "L" {
                rope[0].0 -= 1;
            } else if dir == "R" {
                rope[0].0 += 1;
            }

            for knot in 1..10 {
                if rope[knot-1].0 == rope[knot].0 {
                    if rope[knot-1].1 - rope[knot].1 == 2 {
                        rope[knot].1 += 1;
                    } else if rope[knot].1 - rope[knot-1].1 == 2 {
                        rope[knot].1 -= 1;
                    }
                } else if rope[knot-1].1 == rope[knot].1 {
                    if rope[knot-1].0 - rope[knot].0 == 2 {
                        rope[knot].0 += 1;
                    } else if rope[knot].0 - rope[knot-1].0 == 2 {
                        rope[knot].0 -= 1;
                    }
                } else {
                    // Diagonals...
                    let delta = (rope[knot-1].0 - rope[knot].0, rope[knot-1].1 - rope[knot].1);

                    if delta.0 == 1 && delta.1 == 1 {
                        continue;
                    } else if delta.0 == 2 || delta.0 == -2 || delta.1 == 2 || delta.1 == -2 {
                        if delta.0 > 0 {
                            rope[knot].0 += 1;
                        } else {
                            rope[knot].0 -= 1;
                        }

                        if delta.1 > 0 {
                            rope[knot].1 += 1;
                        } else {
                            rope[knot].1 -= 1;
                        }
                    }
                }
            }

            visited_spaces.insert(rope[9]);
        }
    }

    return visited_spaces.len();
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = part1(&input);
    println!("part 1: {}\n", answer1);

    let answer2 = part2(&input);
    println!("part 2: {}\n", answer2);

    return Ok(());
}
