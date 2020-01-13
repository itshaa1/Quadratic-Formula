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
        prime = factors[i-1] ** 0.5
        if prime % 1 == 0:
            square_numbers.append(factors[i-1])
            largest_square = factors[i-1]
            squared_largest = largest_square ** 0.5 
    
    square_numbers.remove(1)
    if len(square_numbers) == 0:
        return "sqrt(" + str(num) + ")"

    for item in range(len(factors)):
        if factors[item] *  largest_square == num:
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
        prime = factors[i-1] ** 0.5
        if prime % 1 == 0:
            square_numbers.append(factors[i-1])
            largest_square = factors[i-1]
            squared_largest = largest_square ** 0.5
   
    square_numbers.remove(1)
    if len(square_numbers) == 0:
        return "sqrt(" + str(-num) + ")"

    for item in range(len(factors)):
        if factors[item] *  largest_square == num:
            sqrt_by = factors[item]
    
    simplified = str(int(squared_largest)) + "i " + "sqrt(" + str(sqrt_by) + ")"

    return simplified

