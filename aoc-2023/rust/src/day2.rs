use std::fs::read_to_string;

fn parse_input() -> Vec<String> {
    read_to_string("../input/day2.txt")
        .unwrap()
        .split("\n")
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
}

fn get_num(s: &str) -> u32 {
    s.chars()
    .filter(|x| x.is_numeric())
    .collect::<String>()
    .parse::<u32>().unwrap()
}

fn check_set(set: &str) -> bool {
    let cubes = set.split(",");
    for cube in cubes {
        if cube.contains("red") {
            if get_num(cube) > 12 { return false }
        } else if cube.contains("green") {
            if get_num(cube) > 13 { return false }
        } else {
            if get_num(cube) > 14 { return false }
        }
    }
    true
}

fn part_one(input: &Vec<String>) -> u32 {
    input.iter().fold(0, |acc, line| {
        let line = line.split(":").collect::<Vec<_>>();
        let id = get_num(line[0]);
        let mut is_valid = true;
        for set in line[1].split(";") {
            if !check_set(set) { 
                is_valid = false;
                break;
             };
        }
        if is_valid {
            acc + id
        } else {
            acc
        }
    })
}

#[derive(Debug)]
struct Set {
    red: u32,
    green: u32,
    blue: u32
}

fn check_req<'a>(set: &str, game: &'a mut Set) {
    let cubes = set.split(",");
    for cube in cubes {
        if cube.contains("red") {
            game.red = u32::max(game.red, get_num(cube));
        } else if cube.contains("green") {
            game.green = u32::max(game.green, get_num(cube));
        } else {
            game.blue = u32::max(game.blue, get_num(cube));
        }
    }
}

fn part_two(input: &Vec<String>) -> u32 {
    input.iter().fold(0, |acc, line| {
        let line = line.split(":").collect::<Vec<_>>();
        let mut game = Set { red: 0, green: 0, blue: 0 };
        for set in line[1].split(";") {
            check_req(set, &mut game);
        }
        let power = game.blue * game.green * game.red;
        acc + power
    })
}

pub fn main() {
    let input: &Vec<String> = &parse_input();
    println!("{}", part_one(input));
    println!("{}", part_two(input));
}