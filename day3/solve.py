from functools import reduce
from datetime import datetime


def read_file(filename: str = "coordinates.txt") -> [[chr]]:
    with open(filename) as f:
        return {line: coords for (line, coords) in enumerate(f.read().splitlines())}


def find(right: int, down: int, coord_map: {int: [chr]}) -> int:
    def walk(current_down: int,
             current_right: int,
             tree_count: int) -> int:
        coord_line = coord_map[current_down]
        coord = coord_line[(current_right % len(coord_line))]
        updated_tree_count = tree_count + 1 if coord == '#' else tree_count

        next_down = current_down + down
        if next_down not in coord_map:
            return updated_tree_count
        else:
            return walk(current_down=next_down,
                        current_right=current_right + right,
                        tree_count=updated_tree_count)
    return walk(current_down=down, current_right=right, tree_count=0)


def find_trees(paths: [(int, int)], coordinate_map: {int: [chr]}) -> int:
    trees = map(lambda path: find(path[0], path[1], coordinate_map), paths)
    return reduce(lambda x, y: x * y, trees)


if __name__ == '__main__':

    paths = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    coordinate_map = read_file()
    start = datetime.now()
    solution1 = find(3, 1, coordinate_map)
    solution2 = find_trees(paths, coordinate_map)
    execution_time = datetime.now() - start
    print("Day 3")
    print(f"Part 1 Solution: {solution1}")
    print(f"Part 2 Solution: {solution2}")
    print(f"Took: {execution_time.microseconds / 1000}ms")
