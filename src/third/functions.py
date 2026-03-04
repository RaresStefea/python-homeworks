from __future__ import annotations


def is_even(number: int = 0) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


def maximum(number1: int = 0, number2: int = 0) -> int:
    if number1 > number2:
        return number1
    else:
        return number2


def vowel_count(word: str = "") -> int:
    VOWELS = ("a", "e", "i", "o", "u")
    count = 0
    for i in word:
        if i.lower() in VOWELS:
            count += 1
    return count


def number_exists(input_list: list[str], number: str) -> bool:
    if number in input_list:
        return True
    else:
        return False


def list_sum(input_list: list[int]) -> int:
    return sum(input_list)


def analyze_word(word: str) -> tuple:
    return len(word), vowel_count(word), word.upper()


def number_stats(numbers: list[int]) -> tuple[int, int, float, int] | str:
    if len(numbers) == 0:
        return "No numbers given."
    else:
        count = 0
        for number in numbers:
            if not is_even(number):
                count += 1
        return min(numbers), max(numbers), sum(numbers) / len(numbers), count
