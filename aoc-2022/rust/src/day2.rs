use std::fs;

enum Hand {
    Scissors,
    Paper,
    Rock
}

use Hand::{Scissors, Rock, Paper};

fn parse_line(line: (&str, &str)) -> (Hand, Hand) {
    match line {
        ("A", "X") => (Rock, Rock),
        ("A", "Y") => (Rock, Paper),
        ("A", _) => (Rock, Scissors),
        ("B", "X") => (Paper, Rock),
        ("B", "Y") => (Paper, Paper),
        ("B", _) => (Paper, Scissors),
        (_, "X") => (Scissors, Rock),
        (_, "Y") => (Scissors, Paper),
        (_, _) => (Scissors, Scissors)
    }
}

fn battle(opponent: Hand, me: Hand) -> u32 {
    match (opponent, me) {
        (Rock, Rock) => 1 + 3,
        (Rock, Paper) => 2 + 6,
        (Rock, Scissors) => 3 + 0,
        (Paper, Rock) => 1 + 0,
        (Paper, Paper) => 2 + 3,
        (Paper, Scissors) => 3 + 6,
        (Scissors, Rock) => 1 + 6,
        (Scissors, Paper) => 2 + 0,
        (Scissors, Scissors) => 3 + 3
    }
}

fn part_one(lines: &Vec<(&str, &str)>) -> u32 {
    lines.iter()
        .map(|line| parse_line(*line))
        .fold(0, |acc, elem| acc + battle(elem.0, elem.1))
}

fn reparse_line(line: (&str, &str)) -> (Hand, Hand) {
    match line {
        ("A", "X") => (Rock, Scissors),
        ("A", "Y") => (Rock, Rock),
        ("A", _) => (Rock, Paper),
        ("B", "X") => (Paper, Rock),
        ("B", "Y") => (Paper, Paper),
        ("B", _) => (Paper, Scissors),
        (_, "X") => (Scissors, Paper),
        (_, "Y") => (Scissors, Scissors),
        (_, _) => (Scissors, Rock)
    }
}

fn part_two(lines: &Vec<(&str, &str)>) -> u32 {
    lines.iter()
        .map(|line| reparse_line(*line))
        .fold(0, |acc, elem| acc + battle(elem.0, elem.1))
}

pub fn main() {
    let lines = 
        fs::read_to_string("../input/day2.txt")
        .unwrap();
    let lines = lines
        .split("\n")
        .map(|line| line.split_whitespace().collect::<Vec<_>>())
        .map(|x| (x[0], x[1]))
        .collect::<Vec<_>>();
    println!("{:?}", part_one(&lines));
    println!("{:?}", part_two(&lines));
}
