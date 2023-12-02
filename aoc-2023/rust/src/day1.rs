use std::{fs::read_to_string, collections::HashMap};

fn parse_input() -> Vec<String> {
    read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n")
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
}

fn part_one(input: &Vec<String>) -> u32 {
    input
        .iter()
        .map(|x| x.chars())
        .map(|x| x.filter(|x| x.is_numeric()))
        .map(|x| x.collect::<String>())
        .map(|x| x[..1].to_string() + &x[x.len()-1..].to_string())
        .map(|x| x.parse::<u32>().unwrap())
        .sum::<u32>()
}

// const DIGITS: [&'static str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

// fn find_digit(x: &str, rev: bool, digits: &HashMap<&str, String>) -> String {
//     let n = x.len() - 1;
//     for i in 0..=n {
//         let slice = if rev { &x[n-i ..] } else { &x[..i] };
//         for (i, digit) in DIGITS.iter().enumerate() {
//             let num = (i+1).to_string();
//             if slice.contains(digit) {
//                 return digits.get(digit).unwrap().to_string();
//             } else if slice.contains(&num) {
//                 return num;
//             }
//         }
//     }
//     String::new()
// }

// fn part_two(input: &Vec<String>) -> u32 {
//     let mut digits = HashMap::new();
//     for (i, digit) in DIGITS.iter().enumerate() {
//         digits.insert(*digit, (i+1).to_string());
//     }
//     input
//         .iter()
//         .map(|x| {
//             let mut first = find_digit(&x, false, &digits);
//             let last = find_digit(&x, true, &digits);
//             if first.is_empty() { first = last.clone() };
//             first + &last
//         })
//         .map(|x| x.parse::<u32>().unwrap())
//         .sum::<u32>()
// }

fn part_two(input: &Vec<String>) -> u32 {
    let tmp = input
        .iter()
        .map(|x| {
            let x = x.replace("one", "o1e");
            let x = x.replace("two", "t2o");
            let x = x.replace("three", "t3e");
            let x = x.replace("four", "f4r");
            let x = x.replace("five", "f5e");
            let x = x.replace("six", "s6x");
            let x = x.replace("seven", "s7n");
            let x = x.replace("eight", "e8t");
            let x = x.replace("nine", "n9e");
            x
        })
        .collect::<Vec<_>>();
    tmp
        .iter()
        .map(|x| x.chars())
        .map(|x| x.filter(|x| x.is_numeric()))
        .map(|x| x.collect::<String>())
        .map(|x| x[..1].to_string() + &x[x.len()-1..].to_string())
        .map(|x| x.parse::<u32>().unwrap())
        .sum::<u32>()
}

pub fn main() {
    let input = &parse_input();
    println!("{}", part_one(input));
    println!("{}", part_two(input));
}