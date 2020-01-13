#importing math module, simplifying radical program, and standard to vertex program
from math import *
from simplify_radical import *
from standard_to_vertex import *

#finding a, b, and c of quadratic equation
a = int(input("enter a: "))
b = int(input("enetr b: "))
c = int(input("enter c: "))

#the quadratic discriminant(what's being square rooted)
quadDiscrim = b ** 2 - 4 * a * c

#this is for the unfactored equation that will be printed
notReducedTop = str(-b) + " ±sqrt(" + str(quadDiscrim) +  ")" #top of the equation
notReducedBottom = str(2 * a) #bottom divided by of the equation
unfactored_equation = notReducedTop + "/" + notReducedBottom #making the equation

#if a is then you get ZeroDivisionError because its a linear function
if a == 0:
    raise ZeroDivisionError("a is 0 so its a linear function, however, the quadratic discriminant is " + str(quadDiscrim) + "  and the equation is " + equation)

#if the quadratic discriminant is larger than 0, you will have 2 real answers
if quadDiscrim > 0:
    posAnswer = (-b + sqrt(quadDiscrim))/(2 * a) #calculating positive answer
    negAnswer = (-b - sqrt(quadDiscrim))/(2 * a) #calculating negative answer
    factored_equation = str(-b) + " ± " + pos_simplify(quadDiscrim) + "/" + notReducedBottom #the factored equation
    print("Two Real Answers")

#if the quadratic discrimant is less than 0, you will have two imaginary answers
elif quadDiscrim < 0:
    posAnswer, negAnswer = (-b + quadDiscrim ** 0.5)/(2 * a), (-b - quadDiscrim ** 0.5)/(2 * a) #I tried switchting it up for finding pos and negAnswer on this one, is this a good idea?
    factored_equation = str(-b) + " ± " + neg_simplify(quadDiscrim) + "/" + notReducedBottom #factored equation
    print("Two Imgainary Roots")

#if the quadratic discriminant is 0, than you will have 1 real answer
else:
    posAnswer, negAnswer = (-b)/(2 * a), (-b)/(2 * a) #the one line switch up again
    factored_equation = str(-b) + "/" + notReducedBottom #just the factored equation
    print("One Real Answer")

#all the ending print statements
print("The Vertex form of the equation is: " + standard_to_vertex(a, b, c)) #prints vertex form of equation
print("The positive answer is: " + str(posAnswer)) #prints positive answer
print("The negative answer is: " + str(negAnswer)) #prints negative answer
print("The unfactored equation is: " + unfactored_equation) #prints unfactored equation
print("The factored equation is: " + factored_equation) #prints factored equation


