use std::cell::RefCell;
use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/21-sample.txt";
    const FILE_NAME: &str = "input/21-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

#[derive(Debug)]
struct Entry {
    name: String,
    op: Option<String>,
    left: Option<String>,
    right: Option<String>,
    val: Option<i64>,
    checked: bool,
}

fn part1(input: &[String]) -> i64 {
    let mut entries: HashMap<String, RefCell<Entry>> = HashMap::new();
    let mut num_with_unknown_values: usize = 0;

    for line in input {
        let first_split = line.split(": ").collect::<Vec<_>>();
        let name = first_split[0].to_string();
        
        let new_entry = match first_split[1].parse::<i64>() {
            Ok(val) => {
                Entry {
                    name: name.clone(),
                    op: None,
                    left: None,
                    right: None,
                    val: Some(val),
                    checked: true,
                }
            },
            Err(_) => {
                let split2 = first_split[1].split(" ").collect::<Vec<_>>();
                num_with_unknown_values += 1;
                Entry {
                    name: name.clone(),
                    op: Some(split2[1].to_string()),
                    left: Some(split2[0].to_string()),
                    right: Some(split2[2].to_string()),
                    val: None,
                    checked: false,
                }
            },
        };

        println!("Entry: {new_entry:?}");

        entries.insert(name, RefCell::new(new_entry));
    }

    while num_with_unknown_values > 0 {
        println!("\n\nnum with unknown values: {}", num_with_unknown_values);

        for (name, entry_ref) in entries.iter() {
            let mut entry = entry_ref.borrow_mut();

            if let Some(_) = entry.val {
                continue;
            } if entry.checked {
                continue;
            } else {
                println!("Need to calculate: {entry:?}");

                let left = entries.get(entry.left.as_ref().unwrap()).unwrap().borrow();
                let right = entries.get(entry.right.as_ref().unwrap()).unwrap().borrow();

                if let (Some(left_val), Some(right_val)) = (left.val, right.val) {
                    let op = entry.op.as_ref().unwrap();
                    entry.val = Some(match op.as_str() {
                        "+" => left_val + right_val,
                        "-" => left_val - right_val,
                        "*" => left_val * right_val,
                        "/" => left_val / right_val,
                        _ => {
                            println!("Error: {entry:?}");
                            0
                        },
                    });
                    num_with_unknown_values -= 1;
                } else {
                    println!("Still not enough info");
                }
            }
        }
    }

    let root = entries.get("root").unwrap().borrow();
    println!("root: {root:?}");

    let result = root.val.unwrap();
    return result;
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
