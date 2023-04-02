def largestPrimeFactor(number):
    
    prime_factors = []
    
    for num in range(number + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                if number % num == 0:
                    print(num)
                    prime_factors.append(num)
          
    print(prime_factors)
            
largestPrimeFactor(600851475143)