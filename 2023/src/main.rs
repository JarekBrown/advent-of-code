// use crate::day1;
use clap::{arg, command, value_parser};
use std::env;

mod day1;

fn main() {
    // let args: Vec<_> = env::args().collect();
    // if args.len() > 1 {}
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
        _ => panic!("no currently valid day provided"),
    }
}
