# Practice

## Number checks
print("Enter your number:")
number = int(input().strip())

if number > 0:
    print("Your number is positive!")
elif number == 0:
    print("Your number is zero!")
elif number < 0:
    print("Your number is negative")

if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")

## Letter checks

print("Enter your letter:")
letter = input().strip()
VOWELS = ["a", "e", "i", "o", "u"]

if letter.isalpha() and len(letter) == 1:
    if letter.lower() in VOWELS:
        print("Your letter is a vowel!")
    else:
        print("Your letter is consonant!")
else:
    print("Not a letter!")

## Sale

print("Enter your age:")
age = int(input().strip())

if (age > 65) and (age < 18):
    print("You benefit from reduced price!")
else:
    print("You don't benefit from a reduced price!")

## Leap year

print("Enter your year:")
year = int(input().strip())

if year % 4 == 0:
    print("This year is a leap year!")
else:
    print("This year is not a leap year!")

# Homework 1

print("Enter your password: ")
password = input().strip()

if (
    (len(password) >= 8)
    and (password.isupper())
    and (any([i.isdecimal() for i in password]))
):
    print("Welcome!")

else:
    print("Password is too weak!")

# Homework 2

print("Enter your word:")
sentence = input().strip()

VOWELS = ["a", "e", "i", "o", "u"]

for i in sentence:
    if i.lower() in VOWELS:
        print(i)
