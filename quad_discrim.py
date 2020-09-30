# importing math module, simplifying radical program, and standard to vertex program
from math import *

import sys

from quadratic_functions import pos_simplify, neg_simplify, standard_to_vertex

# finding a, b, and c of quadratic equation
while True:
    try:
        a = int(input("enter a: "))
        b = int(input("enter b: "))
        c = int(input("enter c: "))
        break
    except Exception as e:
        print(e)

# the quadratic discriminant(what's being square rooted)
quad_disc = b ** 2 - 4 * a * c

# this is for the unfactored equation that will be printed
equation_top = f"{-b} ±sqrt({quad_disc})"
equation_bottom = f"{2 * a}"
unfactored_equation = f"{equation_top}/{equation_bottom}"

# if a is then you get ZeroDivisionError because its a linear function
lin_equation = f"y = {b}x + {c}"
if a == 0:
    sys.exit(f"a is 0 so it's a linear function, however, the quadratic discriminant is "
             f"{quad_disc} and the equation is {lin_equation}")

# if the quadratic discriminant is larger than 0, you will have 2 real answers
if quad_disc > 0:
    pos_answer = (-b + sqrt(quad_disc)) / (2 * a)
    neg_answer = (-b - sqrt(quad_disc)) / (2 * a)
    factored_equation = f"{-b} ± {pos_simplify(quad_disc)}/{equation_bottom}"
    print("Two Real Answers")

# if the quadratic discriminant is less than 0, you will have two imaginary answers
elif quad_disc < 0:
    pos_answer, neg_answer = (-b + quad_disc ** 0.5) / (2 * a), (-b - quad_disc ** 0.5) / (2 * a)
    factored_equation = f"{-b} ± {neg_simplify(quad_disc)}/{equation_bottom}"
    print("Two Imaginary Roots")

# if the quadratic discriminant is 0, than you will have 1 real answer
else:
    answer = (-b) / (2 * a)
    factored_equation = f"{-b}/{equation_bottom}"
    print("One Real Answer")

# all the ending print statements
print(f"The Vertex form of the equation is: {standard_to_vertex(a, b, c)}")
if not quad_disc == 0:
    print(f"The positive answer is: {pos_answer}")
    print(f"The negative answer is: {neg_answer}")
else:
    print(f"The answer is: {answer}")
print(f"The unfactored equation is: {unfactored_equation}")
print(f"The factored equation is: {factored_equation}")
