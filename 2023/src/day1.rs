use std::fs;

pub fn run() {
    let data = read_in();

    let mut value = 0;
    for line in data {
        if line.len() > 1 {
            let first = get_first(line.clone());
            let last = get_last(line.clone());
            let together: i32 = format!("{}{}", first, last)
                .parse()
                .expect("failed to cast to i32");
            value = value + together;
        } else {
            let val = get_first(line.clone());
            let together: i32 = format!("{}{}", val, val)
                .parse()
                .expect("failed to cast to i32");
            value = value + together;
        }
    }
    println!("The sum is: {value}")
}

fn read_in() -> Vec<String> {
    let mut output = Vec::new();
    for line in fs::read_to_string("input.txt")
        .expect("couldn't read file")
        .lines()
    {
        let mut s = convert_from_string(line.to_string());
        s = s.chars().filter(|c| c.is_digit(10)).collect();
        output.push(s)
    }
    output
}

fn get_first(text: String) -> String {
    let out = text
        .chars()
        .next()
        .expect("problem getting first char of {in}");

    String::from(out)
}

fn get_last(text: String) -> String {
    let index = text.len();
    let out = text
        .chars()
        .nth(index - 1)
        .expect("problem getting first char of {in}");

    String::from(out)
}

fn convert_from_string(text: String) -> String {
    let string_forms: [&str; 9] = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];
    let num_forms: [&str; 9] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];

    let n = string_forms.len();
    let mut out = text;
    for i in 0..n {
        loop {
            if out.contains(string_forms[i]) {
                let start_index = out.find(string_forms[i]).unwrap() + 1;
                out.replace_range(start_index..start_index, num_forms[i]);
            } else {
                break;
            }
        }
    }
    out
}
