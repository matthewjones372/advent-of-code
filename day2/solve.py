from collections import Counter, namedtuple
from typing import Callable

password_entry = namedtuple(
    "password_entry", ["min_count", "max_count", "char", "password_counter", "password_list"]
)


def read_file(filename: str = "passwords.txt") -> [str]:
    with open(filename) as f:
        return f.read().splitlines()


def parse_entry(line: str) -> password_entry:
    rule, char_and_password = line.split(" ", 1)
    min_count, max_count = rule.split("-")
    char, password = char_and_password.split(":")
    return password_entry(min_count=int(min_count),
                          max_count=int(max_count),
                          char=char,
                          password_counter=(Counter(password)),
                          password_list=list(password))


def check(entries: [password_entry],
          validation_rule: Callable[[password_entry], bool]) -> int:
    return sum([validation_rule(parse_entry(entry)) for entry in entries])


def validation_rule_1(entry: password_entry) -> bool:
    count = entry.password_counter[entry.char]
    return entry.min_count <= count <= entry.max_count


def validation_rule_2(entry: password_entry) -> bool:
    first_char = entry.password_list[entry.min_count]
    second_char = entry.password_list[entry.max_count]
    return (first_char == entry.char and second_char != entry.char) or \
           (second_char == entry.char and first_char != entry.char)


if __name__ == '__main__':
    print("Day 2")
    password_entries = read_file()
    print(f"Part 1: Solution = {check(password_entries, validation_rule_1)}")
    print(f"Part 2: Solution = {check(password_entries, validation_rule_2)}")
