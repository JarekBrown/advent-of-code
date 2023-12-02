use clap::{arg, command, value_parser};
use std::env;

mod day1;
mod day2;

fn main() {
    let args = command!()
        .arg(
            arg!(--day <NUMBER> "which day is being compiled")
                .required(true)
                .value_parser(value_parser!(i32)),
        )
        .get_matches();
    if let Some(day) = args.get_one::<i32>("day") {
        handler(day);
    }
}

fn handler(arg: &i32) {
    match arg {
        1 => day1::run(),
        2 => day2::run(),
        _ => panic!("no currently valid day provided"),
    }
}
