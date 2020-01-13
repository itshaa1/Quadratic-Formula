#Reminder: vertex form is  a(x-h)^2 + k + c
def standard_to_vertex(a, b, c):
    #the equation for finding h is b/2 * -a so this finds it 
    h = (b) / (2 * -a)

    #I honestly forgot why this works here, maybe its wrong?
    step1 = a * (0 + -h) ** 2
    step2 = step1 + c

    #finding k
    if step2 <= -1:
        k = c + step2
    else:
        k = c - step2
    
    #making the vertex equation
    equation = "y = " + str(a) + "(x + " + str(-h) + ")^2 + " + str(k + c)  
    return equation



