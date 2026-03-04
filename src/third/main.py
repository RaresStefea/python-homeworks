from .functions import (
    is_even,
    vowel_count,
    maximum,
    number_exists,
    list_sum,
    analyze_word,
)
from .functions2 import (
    eliminate_dupes,
    oldest_person,
    freq,
    text_appear,
    switch_dict,
    merger,
    dicti_ops,
)
import re


print("Enter a number:")
number = int(input().strip())
print("Is your number even? {0}".format("Yes" if is_even(number) else "No."))

print("Enter number 1:")
first = int(input().strip())

print("Enter number 2:")
second = int(input().strip())

print("Number {0} is bigger".format(maximum(first, second)))

print("Enter a string:")
word = input().strip()
print("The number of vowels is {0}.".format(vowel_count(word)))

print("Enter a list of numbers:")

initial_word = input().strip(" ,")
split_list = [int(x) for x in re.split(r"[,\s;]+", initial_word)]
print("Your total sum is {0}".format(list_sum(split_list)))

print("Enter your number:")
magic_number = input().strip()
print("Enter your list:")
input_list = input().strip()
split_list2 = [x for x in re.split(r"[,\s;]+", input_list)]
print(
    "Your number {0} in the list.".format(
        "exists" if number_exists(split_list2, magic_number) else "doesn't exist"
    )
)

print("Enter your word:")
word = input().strip()

print("Length: {0} \nVowels: {1} \nUppercase: {2}".format(*analyze_word(word)))

print("Enter a list of numbers:")
initial_word = input().strip(" ,")
split_list = [int(x) for x in re.split(r"[,\s;]+", initial_word)]
result = split_list
if type(result) is str:
    print(result)
else:
    print(
        "Smallest number: {0} \nLargest number: {1}\nAvg: {2}\nOdd numbers: {3}".format(
            *result
        )
    )

dupe_list = [1, 2, 2, "Me", "ME", "Me", 3, 4, 2]
print(eliminate_dupes(dupe_list))

old_list = [("Rares", 22), ("Ion", 15), ("Matei", 40)]
print(oldest_person(old_list))

count_tuple = [1, 1, 1, 1, 2, 2, 3, 2, 3]
print(freq(count_tuple))

text = "apple banana apple orange banana apple"
text_appear(text)

dictionar = {"Rares": 18, "Matei": 20}
print("Switcheroo: {0}".format(switch_dict(dictionar)))

list1 = [(1, "apple"), (3, "orange"), (5, "banana")]
list2 = [(2, "grape"), (4, "kiwi"), (6, "melon")]

print("Sorted list is {0}".format(merger(list1, list2)))

people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"},
}

print("Oldest person is {0} aged: {1}".format(*dicti_ops(people)))
