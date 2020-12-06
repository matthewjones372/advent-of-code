from collections import namedtuple, defaultdict

BoardingPass = namedtuple(
    "BoardingPass", ["seat_id", "seat_number", "row_number"]
)


def read_file(filename: str = "boarding_passes.txt"):
    with open(filename) as f:
        return f.read().splitlines()


def search(rows: [chr], search_range: (int, int), split_on: chr) -> int:
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


def find_row(rows: [str]) -> int:
    return search(rows, (0, 127), split_on='F')


def find_seat(seats: [str]) -> int:
    return search(seats, (0, 7), split_on='L')


def get_seat_id(seat_number: int, row_number: int) -> int:
    return (row_number * 8) + seat_number


def parse_boarding_pass(boarding_pass_str: str) -> BoardingPass:
    row = find_row(boarding_pass_str[:7])
    seat = find_seat(boarding_pass_str[7:])
    seat_id = get_seat_id(seat, row)
    return BoardingPass(seat_id=seat_id, seat_number=seat, row_number=row)


def parse_boarding_passes(boarding_passes_str: [str]) -> [BoardingPass]:
    return list(map(parse_boarding_pass, boarding_passes_str))


def get_highest_seat_id(boarding_passes: [BoardingPass]) -> int:
    return max(boarding_passes, key=lambda boarding_pass: boarding_pass.seat_id).seat_id


def find_missing_seat_id(boarding_passes: [BoardingPass]) -> int:
    seating_ids = list(map(lambda p: p.seat_id, boarding_passes))
    min_seat_no = min(seating_ids)
    max_seat_no = max(seating_ids)

    def not_before(seat_id):
        return (seat_id - 1) in seating_ids

    def not_after(seat_id):
        return (seat_id + 1) in seating_ids

    def not_in(seat_id):
        return seat_id not in seating_ids

    for seat_id in range(min_seat_no, max_seat_no):
        if not_in(seat_id) and not_before(seat_id) and not_after(seat_id):
            return seat_id


if __name__ == '__main__':
    boarding_passes = parse_boarding_passes(read_file())
    print(f"Part 1 Solution : {get_highest_seat_id(boarding_passes)}")
    print(f"Part 2 Solution : {find_missing_seat_id(boarding_passes)}")