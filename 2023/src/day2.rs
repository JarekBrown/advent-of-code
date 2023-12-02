use std::collections::VecDeque;
use std::fs;

// constants needed for part 1
const RED: i32 = 12;
const GREEN: i32 = 13;
const BLUE: i32 = 14;

/// ## Runner for Day 2
pub fn run() {
    let data = read_in();

    let mut total = 0;
    for line in data {
        total += split_line(line);
    }
    println!("The sum is: {total}")
}

fn read_in() -> Vec<String> {
    //! reads in file
    let mut output = Vec::new();
    for line in fs::read_to_string("data/day2.txt")
        .expect("couldn't read file")
        .lines()
    {
        let s = String::from(line);
        output.push(s);
    }
    output
}

fn split_line(input: String) -> i32 {
    //! splits the line for comparison of each game, returns score for associated part
    let mut text = input.clone();
    text.retain(|c| !r#"(),".;:'"#.contains(c));
    let mut out: VecDeque<&str> = text.split(' ').collect();
    // part 1:
    // let value: i32 = out
    //     .get(1)
    //     .expect("failed unwrap game value")
    //     .parse()
    //     .expect("failed to parse game value");

    // if validity_check(&mut out.split_off(2)) {
    //     println!("{}", &value);
    //     return value;
    // } else {
    //     return 0;
    // }

    // part 2:
    game_power(&mut out.split_off(2))
}

fn validity_check(line: &mut VecDeque<&str>) -> bool {
    //! determines if game is valid for part 1
    while !line.is_empty() {
        let count: i32 = line
            .pop_front()
            .unwrap()
            .parse()
            .expect("failed to parse count");
        let color = String::from(line.pop_front().unwrap());
        match color.as_str() {
            "red" => {
                if count > RED {
                    return false;
                }
            }
            "green" => {
                if count > GREEN {
                    return false;
                }
            }
            "blue" => {
                if count > BLUE {
                    return false;
                }
            }
            _ => {}
        }
    }
    true
}

fn game_power(line: &mut VecDeque<&str>) -> i32 {
    //! finds power of each game for part 2
    let mut max_green = 0;
    let mut max_red = 0;
    let mut max_blue = 0;
    while !line.is_empty() {
        let count: i32 = line
            .pop_front()
            .unwrap()
            .parse()
            .expect("failed to parse count");
        let color = String::from(line.pop_front().unwrap());
        match color.as_str() {
            "red" => {
                if count > max_red {
                    max_red = count
                }
            }
            "green" => {
                if count > max_green {
                    max_green = count
                }
            }
            "blue" => {
                if count > max_blue {
                    max_blue = count
                }
            }
            _ => {}
        }
    }

    max_blue * max_red * max_green
}
