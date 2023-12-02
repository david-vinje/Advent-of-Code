use std::{fs::read_to_string, collections::HashMap};

fn parse_input() -> String {
    read_to_string("../input/day1.txt")
        .unwrap()
}

fn part_one(input: &String) {
    let x = input
        .split("\n")
        .map(|x| x.chars())
        .map(|x| x.filter(|x| x.is_numeric()))
        .map(|x| x.collect::<String>())
        .map(|x| x[..1].to_string() + &x[x.len()-1..].to_string())
        .map(|x| x.parse::<u32>().unwrap())
        .sum::<u32>();
    println!("{:?}", x)
}

const DIGITS: [&'static str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

fn find_digit(x: &str, rev: bool, digits: &HashMap<&str, String>) -> String {
    let n = x.len() - 1;
    for i in 0..=n {
        let slice = if rev { &x[n-i ..] } else { &x[..i] };
        for (i, digit) in DIGITS.iter().enumerate() {
            let num = (i+1).to_string();
            if slice.contains(digit) {
                return digits.get(digit).unwrap().to_string();
            } else if slice.contains(&num) {
                return num;
            }
        }
    }
    String::new()
}

fn part_two(input: &String) {
    let mut digits = HashMap::new();
    for (i, digit) in DIGITS.iter().enumerate() {
        digits.insert(*digit, (i+1).to_string());
    }
    let x = input
        .split("\n")
        .map(|x| {
            let mut first = find_digit(&x, false, &digits);
            let last = find_digit(&x, true, &digits);
            if first.is_empty() { first = last.clone() };
            first + &last
        })
        .map(|x| x.parse::<u32>().unwrap())
        .sum::<u32>();
    println!("{:?}", x)
}

pub fn main() {
    let input = &parse_input();
    part_one(input);
    part_two(input);
}