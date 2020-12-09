from __future__ import annotations

import copy
from enum import Enum, unique
from typing import *


@unique
class Instruction(Enum):
    ACC = 'acc'
    JMP = 'jmp'
    NOP = 'nop'

    @staticmethod
    def from_str(instruction: str) -> Instruction:
        if instruction == 'acc':
            return Instruction.ACC
        elif instruction == 'jmp':
            return Instruction.JMP
        elif instruction == 'nop':
            return Instruction.NOP
        else:
            raise ValueError('Instruction does not exist')


class VisitedInstruction:
    __slots__ = ['indexes']

    def __init__(self, indexes: FrozenSet[int]):
        self.indexes = indexes

    @staticmethod
    def empty() -> VisitedInstruction:
        return VisitedInstruction(frozenset())

    def add(self, value: int) -> VisitedInstruction:
        return VisitedInstruction(self.indexes.union([value]))

    def __contains__(self, item: int) -> bool:
        return item in self.indexes


GameInstructions = List[Tuple[Instruction, int]]


def read_file(filename: str = 'game_instructions.txt') -> GameInstructions:
    with open(filename) as f:
        game_instructions = []
        for instruction_str in f.read().splitlines():
            instruction, op = instruction_str.split()
            game_instructions.append((Instruction.from_str(instruction), int(op)))
        return game_instructions


def run_game(game_instructions: GameInstructions) -> (int, bool):
    last_instruction_index = len(game_instructions)

    def go(current_index: int, acc: int, visited: VisitedInstruction) -> (int, bool):
        if current_index == last_instruction_index:
            return acc, True

        if current_index in visited:
            return acc, False

        instruction, op = game_instructions[current_index]

        if instruction is Instruction.NOP:
            return go(current_index + 1, acc, visited.add(current_index))

        if instruction is Instruction.JMP:
            return go(current_index + op, acc, visited.add(current_index))

        if instruction is Instruction.ACC:
            return go(current_index + 1, acc + op, visited.add(current_index))

    return go(current_index=0, acc=0, visited=VisitedInstruction.empty())


def find_broken_instruction(game_instructions: GameInstructions) -> Optional[int]:
    def swap(index: int, current_instruction: Instruction, current_op: int) -> GameInstructions:
        game = copy.copy(game_instructions)
        if current_instruction is Instruction.JMP:
            game[index] = (Instruction.NOP, current_op)
        if current_instruction is Instruction.NOP:
            game[index] = (Instruction.JMP, current_op)
        return game

    for i, (instruction, op) in enumerate(game_instructions):
        if instruction is not Instruction.ACC:
            fixed_game = swap(i, instruction, op)
            acc, is_successful_run = run_game(fixed_game)

            if is_successful_run:
                print(f"Broken Instruction at offset: {i} -> {instruction.value, op}")
                return acc
    else:
        return None


if __name__ == '__main__':
    instructions = read_file()
    print(f"Part 1 Solution: Acc = {run_game(instructions)[0]}")
    print(f"Part 2")
    print(f"Solution: Acc = {find_broken_instruction(instructions)}")
