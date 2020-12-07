import re
from collections import defaultdict

outer_bag_re = re.compile(r'(\w+ \w+) bags contain (.*)')
bag_re = re.compile(r'(\d+) (\w+ \w+) bags?')


def read_file(filename: str = "bag_rules.txt"):
    with open(filename) as f:
        bag_dict = defaultdict(set)
        for rule in f.read().splitlines():
            outer_bag = outer_bag_re.findall(rule)[0][0]
            for count, bag in bag_re.findall(rule):
                bag_dict[bag].add((int(count), outer_bag))
        return bag_dict


def get_outer_bags(rule_dict, root_bag='shiny gold'):
    collected_bags = defaultdict(int)

    def inner(root):
        for count, bag in rule_dict[root]:
            current_count = collected_bags[bag]
            collected_bags[bag] = (current_count + count)
            inner(bag)

    inner(root_bag)
    return len(collected_bags), sum(collected_bags.values())


if __name__ == '__main__':
    bags = read_file()
    print(get_outer_bags(bags))
