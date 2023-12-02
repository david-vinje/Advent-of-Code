use std::fs;
use std::collections::HashSet;

pub fn part_one() -> i32 {
    let mut entries = HashSet::<i32>::new();
    let list = fs::read_to_string("../input/day1.txt").unwrap();
    let list = list.split("\n").map(|x| x.parse().unwrap());
    for a in list {
        let b = 2020 - a;
        if entries.contains(&b) {
            return a * b;
        } else {
            entries.insert(a);
        }
    }
    return -1;
}

pub fn part_two() -> i32{
    let mut entries = HashSet::<i32>::new();
    let list = fs::read_to_string("../input/day1.txt").unwrap();
    let list: Vec<i32> = list.split("\n").map(|x| x.parse().unwrap()).collect();
    for item in list.iter() {
        entries.insert(*item);
    };
    for a in list.iter() {
        for b in list.iter() {
            let c = 2020 - a - b;
            if entries.contains(&c) {
                return a * b * c;
            } 
        }
    }
    return -1;
}