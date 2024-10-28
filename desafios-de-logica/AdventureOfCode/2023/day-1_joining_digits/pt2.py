from utils import read_file


def replace_words(text: str) -> str:
    base = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven": "s7n",
            "eight": "e8t",
            "nine": "n9e"
        }

    for word in base.keys():
        if word in text:
            text = text.replace(word, base.get(word))
    return text


def get_digits(text: str) -> int:
    text_replaced = replace_words(text)

    numbers_in_line = [digit for digit in text_replaced if digit.isdigit()]
    return int(numbers_in_line[0] + numbers_in_line[-1])


def solve_puzzle():
    data = read_file('AdventureOfCode/2023/inputs/day1.txt')
    total = 0
    for line in data:
        print(get_digits(line))
        total+= get_digits(line)
    return total

print(solve_puzzle())
