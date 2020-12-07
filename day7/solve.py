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
    outer_bags = defaultdict(lambda: 1)

    def inner(root):
        for bag_count, bag in rule_dict[root]:
            outer_bags[bag] = outer_bags[bag] * bag_count
            inner(bag)

    inner(root_bag)
    return len(outer_bags), sum(outer_bags.values())


def get_inner_bags(rules, root_bag='shiny gold'):
    return sum([bag_count * (1 + get_inner_bags(rules, bag)) for bag_count, bag in rules[root_bag]])


if __name__ == '__main__':
    rules = read_file()
    count = get_outer_bags(rules)
    print(get_inner_bags(rules))
