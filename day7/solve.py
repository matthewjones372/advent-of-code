import re
from collections import defaultdict
from typing import DefaultDict, Set, Tuple

outer_bag_re = re.compile(r'(\w+ \w+) bags contain (.*)')
bag_re = re.compile(r'(\d+) (\w+ \w+) bags?')

RuleDict = DefaultDict[str, Set[Tuple[int, str]]]


def read_file(filename: str = "bag_rules.txt") -> RuleDict:
    with open(filename) as f:
        bag_dict = defaultdict(set)
        for rule in f.read().splitlines():
            outer_bag = outer_bag_re.findall(rule)[0][0]
            for bag_count, bag in bag_re.findall(rule):
                bag_dict[bag].add((int(bag_count), outer_bag))
        return bag_dict


def get_outer_bags(rule_dict: RuleDict, root_bag: str = 'shiny gold') -> int:
    outer_bags = {}

    def inner(root):
        for bag_count, bag in rule_dict[root]:
            outer_bags[bag] = None
            inner(bag)

    inner(root_bag)
    return len(outer_bags)


def get_inner_bags(rule_dict: RuleDict, root_bag: str = 'shiny gold') -> int:
    return sum([bag_count * (1 + get_inner_bags(rule_dict, bag)) for bag_count, bag in rule_dict[root_bag]])


if __name__ == '__main__':
    rules = read_file()
    count = get_outer_bags(rules)
    print(count)
