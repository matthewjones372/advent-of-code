from typing import List, Tuple, Optional
import copy

GameInstructions = List[Tuple[str, int]]


def read_file(filename: str = 'game_instructions.txt') -> GameInstructions:
    with open(filename) as f:
        gameInstructions = []
        for instruction in f.read().splitlines():
            command, number = instruction.split()
            gameInstructions.append((command, int(number)))
        return gameInstructions


def run_game(gameInstructions: GameInstructions) -> (int, bool):

    accumulator = 0
    current_op_index = 0
    last_op_index = len(gameInstructions)
    visited_ops = set()

    while True:
        if current_op_index == last_op_index:
            return accumulator, True

        if current_op_index in visited_ops:
            return accumulator, False

        visited_ops.add(current_op_index)
        current_op, op = gameInstructions[current_op_index]

        if current_op == 'nop':
            current_op_index += 1

        if current_op == 'jmp':
            current_op_index += op

        if current_op == 'acc':
            accumulator += op
            current_op_index += 1


def find_broken_instruction(gameInstructions: GameInstructions) -> Optional[int]:
    for i, (command, count) in enumerate(gameInstructions):
        fixed_game = swap_op(command, count, gameInstructions, i)
        acc, is_successful_run = run_game(fixed_game)

        if is_successful_run:
            return acc
    else:
        return None


def swap_op(command, count, gameInstructions, index):
    fixed_game = copy.deepcopy(gameInstructions)
    if command == 'jmp':
        fixed_game[index] = ('nop', count)
    if command == 'nop':
        fixed_game[index] = ('jmp', count)
    return fixed_game


if __name__ == '__main__':
    instructions = read_file()
    print(f"Part 1 Solution: {run_game(instructions)}")
    print(f"Part 2 Solution: {find_broken_instruction(instructions)}")
