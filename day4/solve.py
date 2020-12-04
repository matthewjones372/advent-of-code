import re

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
match_patterns = re.compile(fr"{'|'.join(required_fields)}")

field_values = re.compile(r'(\w{3}):(\S+)')

eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
eye_colour_re = re.compile(fr"{'|'.join(eye_colours)}")

hcl_re = re.compile(r'^#[\w]{6}$')
passport_re = re.compile(r'^\d{9}')


def read_file(filename: str = "passports.txt") -> [str]:
    with open(filename) as f:
        return [passport for passport in f.read().split("\n\n")]


def passports_with_valid_field_number(passports_list: [str]) -> int:
    return sum(map(has_required_fields, passports_list))


def has_required_fields(passport_str: str, required_fields_n: int = 7) -> bool:
    return len(match_patterns.findall(passport_str)) == required_fields_n


def has_valid_fields(passport_str: str) -> bool:
    if not has_required_fields(passport_str):
        return False

    fields = {field: v for field, v in field_values.findall(passport_str)}

    def is_valid_byr() -> bool:
        return 1920 <= int(fields['byr']) <= 2002

    def is_valid_iyr() -> bool:
        return 2010 <= int(fields['iyr']) <= 2020

    def is_valid_eyr() -> bool:
        return 2020 <= int(fields['eyr']) <= 2030

    def is_valid_ecl() -> bool:
        return True if eye_colour_re.search(fields['ecl']) else False

    def is_valid_hgt() -> bool:
        height = fields['hgt']
        if height.endswith('cm'):
            return 150 <= int(height.strip('cm')) <= 193
        elif height.endswith('in'):
            return 59 <= int(height.strip('in')) <= 76
        else:
            return False

    def is_valid_hcl() -> bool:
        return True if hcl_re.search(fields['hcl']) else False

    def is_valid_pid() -> bool:
        return True if passport_re.search(fields['pid']) else False

    rules = [is_valid_ecl,
             is_valid_byr,
             is_valid_iyr,
             is_valid_eyr,
             is_valid_hgt,
             is_valid_hcl,
             is_valid_pid]

    return all(r() for r in rules)


def passports_with_valid_fields(passports_list):
    return sum(map(has_valid_fields, passports_list)) - 1


if __name__ == '__main__':
    passports = read_file()
    print("Day 4")
    print(f"Solution Part 1 - Valid passports = {passports_with_valid_field_number(passports)}")
    print(f"Solution Part 2 - Valid passports = {passports_with_valid_fields(passports)}")
