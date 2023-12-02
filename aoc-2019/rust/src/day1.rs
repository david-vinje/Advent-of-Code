use std::{fs, ops::Div};

fn compute_fuel(x: i32) -> i32 {
    x.div(3) - 2
}

pub fn part_one() -> i32 {
    fs::read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n")
        .map(|x| {
            compute_fuel(x.parse().unwrap())
        })
        .fold(0, |acc, elem| acc + elem)
}

pub fn part_two() -> i32 {
    fs::read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n")
        .map(|x| {
            let mut x: i32 = compute_fuel(x.parse().unwrap());
            let mut sum = x;
            while compute_fuel(x) > 0 {
                x = compute_fuel(x);
                sum += x;
            }
            return sum;
        })
        .fold(0, |acc, elem| acc + elem)
}
