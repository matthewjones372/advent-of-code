from collections import namedtuple
from typing import Optional, Sequence, Set


BoardingPass = namedtuple(
    "BoardingPass", ["seat_id", "seat_number", "row_number"]
)


def read_file(filename: str = "boarding_passes.txt") -> Sequence[str]:
    with open(filename) as f:
        return f.read().splitlines()


def search(rows: Sequence[chr], search_range: (int, int), split_on: chr) -> int:
    def inner(remaining_rows, lower, upper):
        if remaining_rows:
            head, *tail = remaining_rows
            sub_section = int((lower + upper + 1) / 2)
            if head == split_on:
                return inner(tail, lower, sub_section - 1)
            else:
                return inner(tail, sub_section, upper)
        return lower

    lower_initial, upper_initial = search_range
    return inner(rows, lower_initial, upper_initial)


def find_row(rows: Sequence[str]) -> int:
    return search(rows, (0, 127), split_on='F')


def find_seat(seats: Sequence[str]) -> int:
    return search(seats, (0, 7), split_on='L')


def get_seat_id(seat_number: int, row_number: int) -> int:
    return (row_number * 8) + seat_number


def parse_boarding_pass(boarding_pass_str: str) -> BoardingPass:
    row = find_row(boarding_pass_str[:7])
    seat = find_seat(boarding_pass_str[7:])
    seat_id = get_seat_id(seat, row)
    return BoardingPass(seat_id=seat_id, seat_number=seat, row_number=row)


def parse_boarding_passes(boarding_passes_str: Sequence[str]) -> Set[BoardingPass]:
    return set(map(parse_boarding_pass, boarding_passes_str))


def get_highest_seat_id(boarding_passes: Set[BoardingPass]) -> int:
    return max(boarding_passes, key=lambda boarding_pass: boarding_pass.seat_id).seat_id


def find_missing_seat_id(boarding_passes: Set[BoardingPass]) -> Optional[int]:
    seating_ids = set(map(lambda p: p.seat_id, boarding_passes))
    for seat_id in range(min(seating_ids), max(seating_ids)):
        if is_missing_seat(seat_id, seating_ids):
            return seat_id
    else:
        return None


def is_missing_seat(seat_id: int, seating_ids: Set[int]) -> bool:
    def not_before():
        return (seat_id - 1) in seating_ids

    def not_after():
        return (seat_id + 1) in seating_ids

    def not_in():
        return seat_id not in seating_ids

    return not_in() and not_before() and not_after()


if __name__ == '__main__':
    passes = parse_boarding_passes(read_file())
    print(f"Part 1 Solution : {get_highest_seat_id(passes)}")
    print(f"Part 2 Solution : {find_missing_seat_id(passes)}")
