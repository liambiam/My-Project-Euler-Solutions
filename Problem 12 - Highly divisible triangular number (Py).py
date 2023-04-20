
import math

def divisibleTriangleNumber(n):

    triangle_numbers_factors = []
    i = 1
    
    while True:
        # Generate the ith triangle number
        integers = []
        for j in range(1,i):
            integers.append(j)
        triangle_number = sum(integers)

        # Getting factors of each triangle number
        factors = []
        for j in range(1, int(math.sqrt(triangle_number)) + 1):
            # Finding factors up to sqrt
            if triangle_number % j == 0:
                factors.append(j)
                # Of those factors, tn / j are also factors above sqrt
                if j != triangle_number // j:
                    factors.append(triangle_number // j)
                    
        # If number of factors >= n, solution found
        number_of_factors = len(factors)
        if number_of_factors >= n:
            triangle_numbers_factors.append(factors)
            break
        i += 1


    print(triangle_number)
    
divisibleTriangleNumber(500)