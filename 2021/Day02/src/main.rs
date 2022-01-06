use std::fs::File;
use std::io::{self, BufReader, BufRead};
use std::path::Path;
// use std::io::{self, prelude::*, BufReader};
/*

struct Result<A, E>{
    enum {
        Ok,
        Error,
    } asdf;
    union {
        A ok;
        E error;
    }
}


*/


fn main() -> Result<(), Error> {
    let file = File::open("input.txt").expect("open file");
    let reader = BufReader::new(file);
    let mut depth = 0;
    let mut horizontal = 0;
    let mut aim = 0;

    for line in reader.lines() {
        let value = line?;
        // expect("lines are good");
        println!("{}", value);
        let (cmd, distance_str) = value.split_once(" ").expect("parse error");
        
        let dist : i64 = distance_str.parse().expect("parse error");
        match cmd {
            "backward" => {
                horizontal -= dist;
            }
            "forward" => {
                horizontal += dist;
                depth += aim * dist;
            }
            "down" => {
                aim += dist;
            }
            "up" => {
                aim -= dist;
            }
            _ => {
                panic!("AHHHHHHH!");
            }
        }
        //  .splitwhitespace();
    }
    println!("{}", horizontal);
    println!("{}", depth);
    println!("{}", horizontal * depth);
}

fn part1() {
    let file = File::open("input.txt").expect("open file");
    let reader = BufReader::new(file);
    let mut depth = 0;
    let mut horizontal = 0;

    for line in reader.lines() {
        let value = line.expect("lines are good");
        println!("{}", value);
        let (cmd, distance_str) = value.split_once(" ").expect("parse error");
        
        let dist : i64 = distance_str.parse().expect("parse error");
        match cmd {
            "backward" => {
                horizontal -= dist;
            }
            "forward" => {
                horizontal += dist;
            }
            "down" => {
                depth += dist;
            }
            "up" => {
                depth -= dist;
            }
            _ => {
                panic!("AHHHHHHH!");
            }
        }
        //  .splitwhitespace();
    }
    println!("{}", horizontal);
    println!("{}", depth);
    println!("{}", horizontal * depth);
}
