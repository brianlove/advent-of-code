use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

use anyhow::{/*Context,*/ Result};

fn read_input() -> Result<Vec<String>> {
    // const FILE_NAME: &str = "input/06-sample.txt";
    const FILE_NAME: &str = "input/06-input.txt";

    let input = File::open(FILE_NAME)?;
    let buffered = BufReader::new(input);

    return buffered
        .lines()
        .map(|line| Ok(line?))
        .collect()
}

// fn part1(input: &[String]) -> usize {
//     let buffer = input[0].to_string().chars().collect::<Vec<char>>();
//     let mut sequence_start: usize = 0;

//     while sequence_start + 4 < buffer.len() {
//         let buf_slice = &buffer[sequence_start..(sequence_start+4)];
//         // println!("{:?}", buf_slice);
//         let set: HashSet<char> = HashSet::from_iter(buf_slice.to_vec());
//         // println!("    {:?}", set);
//         let set_as_vec = Vec::from_iter(set);

//         if set_as_vec.len() == 4 {
//             println!("  > Found start of packet! {}", sequence_start);
//             break;
//         }
//         sequence_start += 1;
//     }

//     return sequence_start + 4;
// }

fn both_parts(input: &[String], packet_size: usize) -> usize {
    let buffer = input[0].to_string().chars().collect::<Vec<char>>();
    let mut sequence_start: usize = 0;

    while sequence_start + packet_size < buffer.len() {
        let buf_slice = &buffer[sequence_start..(sequence_start+packet_size)];
        // println!("{:?}", buf_slice);
        let set: HashSet<char> = HashSet::from_iter(buf_slice.to_vec());
        // println!("    {:?}", set);
        let set_as_vec = Vec::from_iter(set);

        if set_as_vec.len() == packet_size {
            println!("  > Found start of packet! {}", sequence_start);
            break;
        }
        sequence_start += 1;
    }

    return sequence_start + packet_size;
}

fn main() -> Result<()> {
    let input = read_input()?;

    let answer1 = both_parts(&input, 4);
    println!("part 1: {}\n", answer1);

    let answer2 = both_parts(&input, 14);
    println!("part 2: {}\n", answer2);

    return Ok(());
}
