# functions for simplifying positive and negative radicals
def pos_simplify(num):
    if (num ** 0.5) % 1 == 0:
        return str(int(num ** 0.5))
    factors = []
    square_numbers = []
    counter = 1
    while counter <= num:
        if num % counter == 0:
            factors.append(counter)
        counter += 1

    for i in range(len(factors)):
        prime = factors[i - 1] ** 0.5
        if prime % 1 == 0:
            square_numbers.append(factors[i - 1])
            largest_square = factors[i - 1]
            squared_largest = largest_square ** 0.5

    square_numbers.remove(1)
    if len(square_numbers) == 0:
        return "sqrt(" + str(num) + ")"

    for item in range(len(factors)):
        if factors[item] * largest_square == num:
            sqrt_by = factors[item]

    simplified = str(int(squared_largest)) + "sqrt(" + str(sqrt_by) + ")"

    return simplified


def neg_simplify(num):
    num = -num
    if (num ** 0.5) % 1 == 0:
        return str(int(num ** 0.5)) + 'i'
    factors = []
    square_numbers = []
    counter = 1
    while counter <= num:
        if num % counter == 0:
            factors.append(counter)
        counter += 1

    for i in range(len(factors)):
        prime = factors[i - 1] ** 0.5
        if prime % 1 == 0:
            square_numbers.append(factors[i - 1])
            largest_square = factors[i - 1]
            squared_largest = largest_square ** 0.5

    square_numbers.remove(1)
    if len(square_numbers) == 0:
        return "sqrt(" + str(-num) + ")"

    for item in range(len(factors)):
        if factors[item] * largest_square == num:
            sqrt_by = factors[item]

    simplified = str(int(squared_largest)) + "i " + "sqrt(" + str(sqrt_by) + ")"

    return simplified


# function for converting from standard to vertex form
def standard_to_vertex(a, b, c):
    # The equation for finding h is b/2 * -a so this finds it
    h = b / (2 * -a)

    # I honestly forgot why this works here, but it works
    step1 = a * (0 + -h) ** 2
    step2 = step1 + c

    # Finding k
    if step2 <= -1:
        k = c + step2
    else:
        k = c - step2

    # Making the vertex equation
    equation = "y = " + str(a) + "(x + " + str(-h) + ")^2 + " + str(k + c)
    return equation


# function for finding how many real answers there are
def num_real_answers(quad_disc):
    if quad_disc > 0:
        return "Two Real Answers"

    elif quad_disc < 0:
        return "Two Imaginary Roots"

    else:
        return "One Real Answer"


def find_answers(quad_disc, a, b):
    if quad_disc is 0:
        answer = (-b) / (2 * a)
        return answer
    else:
        pos_answer, neg_answer = (-b + quad_disc ** 0.5) / (2 * a), (-b - quad_disc ** 0.5) / (2 * a)
        return pos_answer, neg_answer


def find_unfactored(quad_disc, a, b):
    equation_top = f"{-b} ±sqrt({quad_disc})"
    equation_bottom = f"{2 * a}"
    unfactored_equation = f"{equation_top}/{equation_bottom}"
    return unfactored_equation


def find_factored(quad_disc, a, b):
    if quad_disc > 0:
        equation_bottom = f"{2 * a}"
        factored_equation = f"{-b} ± {pos_simplify(quad_disc)}/{equation_bottom}"
        return factored_equation
    if quad_disc < 0:
        equation_bottom = f"{2 * a}"
        factored_equation = f"{-b} ± {neg_simplify(quad_disc)}/{equation_bottom}"
        return factored_equation
    else:
        equation_bottom = f"{2 * a}"
        factored_equation = f"{-b}/{equation_bottom}"
        return factored_equation

