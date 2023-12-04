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
    // println!("{:?}", symbol_locations);
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
    println!("{:?}", text);
    for (i, item) in text.iter().enumerate() {
        if re.is_match(&item.to_string()) {
            locations.push_back(i);
        }
    }
    println!("Locations: {:?}", locations);
    locations
}

fn score(symbols: &mut VecDeque<VecDeque<usize>>, lines: Vec<String>) -> i32 {
    //! determines valid numbers and returns overall sum
    let mut values: Vec<i32> = Vec::new();
    let re = Regex::new(r"[[\p{N}--[\p{Nd}--[0-9]]]]").unwrap();
    // let mut locs = re.capture_locations();
    for (i, line) in lines.iter().enumerate() {
        println!("i: {i} -- {line}");
        let valid = get_symbols(&mut symbols.clone(), i);
        println!("valid lines: {:?} of length {}", valid, valid.len());
        let re_ops = Regex::new(r"[+\-*/&%$#@=]").unwrap();
        let l: String = re_ops.replace_all(line, ".").to_string();
        println!("{l}");
        let tmp: String = l.split('.').collect();
        // println!("l split: {:?}", l.get(0));
        let mut checked: Vec<usize> = Vec::new();
        for character in l.split('.').into_iter() {
            println!("character: {character}");
            // let already_found: Vec<usize> = Vec::new();
            // let x = line.match_indices(character).collect();
            let (check, j) = repeat_check(line, character, checked.clone());
            if re.is_match(character) && !check {
                // let char_reg = format!(r"[+\-*/&%$#@=]{}[+\-*/&%$#@=]", character);
                // let re_loc = Regex::new(char_reg.as_str()).unwrap();
                // let start_loc = re_loc.find(line).unwrap().start();
                // println!("***j--->{j}");
                // let start = line.find(character).unwrap();
                let start = j;
                let end = start + character.len() - 1;
                println!("start: {start}; end: {end}");
                println!("number starting at {start} and ending at: {end}",);
                if valid.contains(&start) || valid.contains(&end) {
                    let s: String = character.chars().filter(|c| c.is_digit(10)).collect();
                    let val: i32 = s.parse().unwrap();
                    println!("{val} is valid");
                    values.push(val)
                    // } else {
                    //     //
                    //     let k = character.len();
                    //     // line.replace_range(j..k, &gen_string(k));
                }
            }
            checked.push(j);
        }
    }
    let sum: i32 = values.iter().sum();
    println!("{:?}, length:{:?}", values, values.len());
    sum
}

fn get_symbols(symbols: &mut VecDeque<VecDeque<usize>>, n: usize) -> Vec<usize> {
    let mut limit = n;
    let k = symbols.len() - 1;
    // println!("{limit}");
    println!("{:?}", symbols.len() - 1);
    if limit == k {
        println!("upper");
        limit -= 3;
    } else if limit > 1 {
        println!("lower");
        limit -= 1;
    }
    // println!("{:?}", symbols);
    let mut top: VecDeque<usize> = symbols.pop_front().unwrap();
    let mut mid: VecDeque<usize> = symbols.pop_front().unwrap();
    let mut bot: VecDeque<usize> = symbols.pop_front().unwrap();
    // println!("after: {:?}", symbols);
    // println!("{limit}");
    // println!("{:?}", top);
    // println!("lim: {limit}");
    for i in 0..limit {
        top = mid.clone();
        mid = bot.clone();
        bot = symbols.pop_front().unwrap();
        // println!("top: {:?} at {i}", top);
        // println!("after: {:?}", symbols);
    }
    // println!("n: {n}");
    if n == 0 {
        bot = VecDeque::new();
    } else if n == k {
        println!("bottom");
        mid = VecDeque::new();
    }
    let mut lines = vec![top, mid, bot];
    println!("lines: {:?}", lines);
    let mut valid: Vec<usize> = Vec::new();
    for mut l in lines {
        loop {
            println!("l --- {:?}", l);
            if !l.is_empty() {
                let x = l.pop_front().unwrap();
                // println!("anchor: {x}");
                let y = x + 1;
                let z = x - 1;
                // let vals = std::ops::Range { start: z, end: y };
                valid.extend(&[z, x, y]);
            } else {
                break;
            }
        }
    }
    valid
}

fn gen_string(n: usize) -> String {
    let i = 0;
    let mut out = String::new();
    while i < n {
        out.push_str(".");
    }
    out
}

fn repeat_check(line: &String, character: &str, checked: Vec<usize>) -> (bool, usize) {
    let locs: Vec<_> = line.match_indices(character).collect();
    for (i, j) in locs.iter() {
        //
        if !checked.contains(i) {
            return (true, i.clone());
        }
    }
    (false, 0)
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
