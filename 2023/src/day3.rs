use regex::Regex;
use std::collections::VecDeque;
use std::error::Error;
use std::fs;
use std::sync::OnceLock;

static SYMBOLS: OnceLock<Regex> = OnceLock::new();
static NUMBERS: OnceLock<Regex> = OnceLock::new();

/// ## Runner for Day 3
pub fn run() {
    // part 1
    println!("{}", part1("data/day3.txt"));

    // part 2
    // part2(data);
}

fn part1(file: &str) -> i32 {
    SYMBOLS
        .set(Regex::new(r"[+\-*/&%$#@=]").unwrap())
        .expect("failed to set SYMBOLS");
    NUMBERS
        .set(Regex::new(r"[[\p{N}--[\p{Nd}--[0-9]]]]").unwrap())
        .expect("failed to set NUMBERS");
    let lines = read_in(file);
    let mut symbol_locations: VecDeque<VecDeque<usize>> = VecDeque::<VecDeque<usize>>::new();
    for line in &lines {
        let x: VecDeque<&str> = line.rsplit('.').collect();
        symbol_locations.push_back(locate_symbol(line.clone()));
    }
    score_part1(&mut symbol_locations, lines)
}

fn part2(file: &str) -> i32 {
    let lines = read_in(file);
    0
}

fn read_in(path: &str) -> Vec<String> {
    //! reads in file
    let mut output = Vec::new();
    for line in fs::read_to_string(path)
        .expect("couldn't read file")
        .lines()
    {
        let s = String::from(line);

        output.push(s);
    }
    output
}

fn locate_symbol(line: String) -> VecDeque<usize> {
    //! locates symbols and stores their locations
    let mut locations: VecDeque<usize> = VecDeque::new();
    // convert line to chars
    let text: Vec<char> = line.chars().collect();
    for (i, item) in text.iter().enumerate() {
        if SYMBOLS
            .get()
            .expect("failed to get regex from SYMBOLS")
            .is_match(&item.to_string())
        {
            locations.push_back(i);
        }
    }
    locations
}

fn score_part1(symbols: &mut VecDeque<VecDeque<usize>>, lines: Vec<String>) -> i32 {
    //! determines valid numbers and returns overall sum
    let mut values: Vec<i32> = Vec::new();
    for (i, line) in lines.iter().enumerate() {
        let valid = get_symbols(&mut symbols.clone(), i);
        let l: String = SYMBOLS
            .get()
            .expect("failed to get regex from SYMBOLS")
            .replace_all(line, ".")
            .to_string();
        let mut checked: Vec<usize> = Vec::new();
        for character in l.split('.').into_iter() {
            let (check, j) = repeat_check(line, character, checked.clone());
            checked = add_checked(&mut checked, j, character);
            if NUMBERS
                .get()
                .expect("failed to get NUMBERS")
                .is_match(character)
                && check
            {
                let start = j;
                let end = start + character.len() - 1;
                if valid.contains(&start) || valid.contains(&end) {
                    let s: String = character.chars().filter(|c| c.is_digit(10)).collect();
                    let val: i32 = s.parse().unwrap();
                    values.push(val)
                }
            }
        }
    }
    let sum: i32 = values.iter().sum();
    sum
}

fn get_symbols(symbols: &mut VecDeque<VecDeque<usize>>, n: usize) -> Vec<usize> {
    let mut limit = n;
    let k = symbols.len() - 1;
    if limit == k {
        limit -= 2;
    } else if limit > 1 {
        limit -= 1;
    }
    let mut top: VecDeque<usize> = symbols.pop_front().unwrap();
    let mut mid: VecDeque<usize> = symbols.pop_front().unwrap();
    let mut bot: VecDeque<usize> = symbols.pop_front().unwrap();
    for i in 0..limit {
        top = mid.clone();
        mid = bot.clone();
        bot = symbols.pop_front().unwrap();
    }
    if n == 0 {
        bot = VecDeque::new();
    } else if n == k {
        top = VecDeque::new();
    }
    let mut lines = vec![top, mid, bot];
    let mut valid: Vec<usize> = Vec::new();
    for mut l in lines {
        loop {
            if !l.is_empty() {
                let x = l.pop_front().unwrap();
                let y = x + 1;
                let z = x - 1;
                valid.extend(&[z, x, y]);
            } else {
                break;
            }
        }
    }
    valid
}

fn repeat_check(line: &String, character: &str, checked: Vec<usize>) -> (bool, usize) {
    let locs: Vec<_> = line.match_indices(character).collect();
    for (i, j) in locs.iter() {
        if !checked.contains(i) {
            return (true, i.clone());
        }
    }
    (false, 0)
}

fn add_checked(checked: &mut Vec<usize>, index: usize, character: &str) -> Vec<usize> {
    let n = index + character.len();
    for i in index..n {
        checked.push(i);
    }
    checked.to_vec()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn day3_part1() -> Result<(), Box<dyn Error>> {
        assert_eq!(part1("data/day3_test.txt"), 4361);
        Ok(())
    }
}
