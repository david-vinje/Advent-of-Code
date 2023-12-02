use std::fs;
use itertools::Itertools;

pub fn part_one() {
    let res = fs::read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n")
        .map(|x| x.parse::<i32>().unwrap())
        .tuple_windows::<(i32, i32)>()
        .fold(0, |acc, (prev, next)| if prev < next { acc + 1 } else { acc });
    println!("{}", res)
}
pub fn part_two() {
    let res = fs::read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n")
        .map(|x| x.parse::<i32>().unwrap())
        .tuple_windows::<(i32, i32, i32)>()
        .map(|(a, b, c)| a + b + c)
        .tuple_windows::<(i32, i32)>()
        .fold(0, |acc, (prev, next)| if prev < next { acc + 1 } else { acc });
    println!("{}", res)
}
