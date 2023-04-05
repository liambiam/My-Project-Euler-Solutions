def sumSquareDifference(n):

    sum_of_the_squares = sum([i**2 for i in range(1, n+1)])
    square_of_the_sum = sum([i for i in range(1, n+1)]) ** 2
    
    difference = square_of_the_sum - sum_of_the_squares
    
    return difference

sumSquareDifference(10)