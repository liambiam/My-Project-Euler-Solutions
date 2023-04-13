def primeSummation(n):
    # Initialize the sum to zero
    total = 0
    
    # Loop through all odd numbers below n
    for i in range(3, n, 2):
        # Check if i is prime
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        
        # If i is prime, add it to the total
        if is_prime:
            total += i
    
    # Add 2 to the total (2 is a prime number, but we skipped it in the loop)
    total += 2
    
    print(total)
            
        
        

primeSummation(17)