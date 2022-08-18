from typing import List
from math import sqrt


def is_prime(number: List) -> str:
    num = int(number[0])
    if num < 2:
        return "Not"
    i = 2
    while i * i <= num:
        if num % i == 0:
            return "Not"
        i += 1
    return "True"


def factorial(number: List) -> str:
    ans = 1
    for i in range(1, int(number[0]) + 1):
        ans *= i
    return str(ans)


def is_palindrome(input_strings: List) -> str:
    word = ""
    for sub_word in input_strings:
        word += sub_word
    while word != "" and len(word) > 1:
        if word[0] != word[-1]:
            return "Not"
        word = word[1:-1]
    return "Yes"


def has_sqrt(numbers: List) -> str:
    sq = sqrt(int(numbers[0]))
    if sq - int(sq) == 0:
        return "Yes"
    return "Not"


def sum_func(numbers: List) -> str:
    sum = 0
    for number in numbers:
        sum += int(number)
    return str(sum)
