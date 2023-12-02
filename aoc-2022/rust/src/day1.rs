use std::fs;

fn compute_calories() -> Vec<usize> {
    fs::read_to_string("../input/day1.txt")
        .unwrap()
        .split("\n\n")
        .map(|x| x.split('\n')
            .map(|x| x.trim().parse::<usize>().unwrap())
            .sum::<usize>())
        .collect()
}

fn part1() -> usize {
    *compute_calories()
        .iter()
        .max()
        .unwrap()
}

fn part2() -> usize {
    let mut res = compute_calories();
    res.sort_by(|a, b| b.cmp(a));
    res[0] + res[1] + res[2]
}

pub fn main() {
    println!("{}", part1());
    println!("{}", part2());
}