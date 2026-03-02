# Addition Opertor: +
print("Addition:", 5 + 2)  # R: 7

# Subtraction Operator: -
print("Subtraction:", 5 - 2)  # R:3

# Multiplication Operator: *
print("Multiplication:", 5 * 2)  # R:10

# Division Operator: /
print("Division:", 5 / 2)  # R: 2.5

# Floor Division: //
print("Floor:", 5 // 2)  # R:2

# Modulo Operator: %
print("Modulo:", 5 % 2)  # R:5

# Power Operator: **
print("Power:", 5**2)  # R: 25

# Assignment Operator: =
x = 5

print("Assignment:", x)

# Addition Assignment : +=
x += 1

print("Addition:", x)

# Subtraction Assignment: -=
x -= 1

print("Subtraction:", x)

# Multiplication Assignment: *=
x *= 2

print("Multiplication:", x)

# Division Assignment: /=
x /= 2

print("Division:", x)

# Remainder Assignment: %=
x %= 3

print("Remainder:", x)

# Exponent Assignment: **=
x **= 2

print("Exponent:", x)

# Is Equal To: ==

print("Is eq:", x == 2)

# Not Equal To: !=

print("Not Eq:", x != 2)

# Greater Than: >

print("Greater Than:", x > 2)

# Lesser Than: <
print("Lesser Than:", x < 2)

# Greater Than or Equal To: >=
print("Greater Than or eq:", x >= 4)

# Less Than or Equal To: <=
print("Less Than or eq:", x <= 4)

# LOGICAL AND

print("Logical and:", (x > 2) and (x < 10))

# Logical OR
print("Logical OR:", (x > 5) or (x < 10))

# Logical NOT
print("Logical NOT:", not (x < 10))

# Bitwise AND
a = 10  # 0000 1010
b = 4  # 0000 0100
print("Bit AND:", a & b)

# Bitwise OR
print("Bit OR:", a | b)

# Bitwise NOT
print("Bit NOT:", ~a)

# Bitwise XOR
print("Bit XOR:", a ^ b)

# Bitwise right shift
print("Bit shift r:", a >> 2)

# Bitwise left shift
print("Bit shift l:", a << 2)

# is
x1 = 5
y1 = 3

x2 = x1
y2 = y1

print("is:", x1 is x2)
print("is:", x1 is y1)
# is not
print("is:", x1 is not x2)
print("is:", x1 is not y1)

# in
l1 = [5]
print("in:", 5 in l1)

# not in
print("not in:", 5 not in l1)

# matrix multiplicatiom

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("matrix multiplication @:", A @ B)

# walrus operator

print("Walrus:", (n := len([1, 2])) > 4)

# EXERCISE 2
print("Is var1 bigger than var2?")
print("Enter the first number:")
var1 = input()
print("Enter the second number:")
var2 = input()
print(var1 > var2)

# EXERCISE 3
import operator

print("Calculator")
print("Enter the first number:")
op1 = input()
print("Enter the second number:")
op2 = input()
print("Enter operation (+, -, *, /):")

operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

print(
    "Result:",
    (
        ((operation := input()) not in operations)
        and "Operator not allowed / doesn't exist!"
    )
    or operations[operation](int(op1), int(op2)),
)
