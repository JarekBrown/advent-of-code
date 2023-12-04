use regex::Regex;
use std::collections::VecDeque;
use std::error::Error;
use std::fs;

/// ## Runner for Day 3
pub fn run() {
    // part 1
    println!("{}", part1("data/day3.txt"));

    // part 2
    // part2(data);
}

fn part1(file: &str) -> i32 {
    let lines = read_in(file);
    let mut symbol_locations: VecDeque<VecDeque<usize>> = VecDeque::<VecDeque<usize>>::new();
    for line in &lines {
        let x: VecDeque<&str> = line.rsplit('.').collect();
        symbol_locations.push_back(locate_symbol(line.clone()));
    }
    score(&mut symbol_locations, lines)
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
    let re = Regex::new(r"[+\-*/&%$#@=]").unwrap();
    // convert line to chars
    let text: Vec<char> = line.chars().collect();
    for (i, item) in text.iter().enumerate() {
        if re.is_match(&item.to_string()) {
            locations.push_back(i);
        }
    }
    locations
}

fn score(symbols: &mut VecDeque<VecDeque<usize>>, lines: Vec<String>) -> i32 {
    //! determines valid numbers and returns overall sum
    let mut values: Vec<i32> = Vec::new();
    let re = Regex::new(r"[[\p{N}--[\p{Nd}--[0-9]]]]").unwrap();
    for (i, line) in lines.iter().enumerate() {
        let valid = get_symbols(&mut symbols.clone(), i);
        let re_ops = Regex::new(r"[+\-*/&%$#@=]").unwrap();
        let l: String = re_ops.replace_all(line, ".").to_string();
        let tmp: String = l.split('.').collect();
        let mut checked: Vec<usize> = Vec::new();
        for character in l.split('.').into_iter() {
            let (check, j) = repeat_check(line, character, checked.clone());
            checked = add_checked(&mut checked, j, character);
            if re.is_match(character) && check {
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
        // part1("data/day3_test.txt");
        assert_eq!(part1("data/day3_test.txt"), 4361);
        Ok(())
    }
}
