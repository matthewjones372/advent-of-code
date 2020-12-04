import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
match_patterns = re.compile(fr"{'|'.join(required_fields)}")


def read_file(filename: str = "passports.txt"):
    with open(filename) as f:
        return [passport for passport in f.read().split("\n\n")]


def is_valid(passport):
    matched = match_patterns.findall(passport)
    return len(matched) == 7


def valid_passports(passports):
    return sum(map(is_valid, passports))


if __name__ == '__main__':
    passports = read_file("passports.txt")
    print(valid_passports(passports))
