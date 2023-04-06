def prime_check(n):
    """ Sieve of Eratosthenes - Function to check if a number is prime"""
    # 0,1 are not prime
    if n <= 1:
        return False
    # 2,3 are prime
    elif n <= 3:
        return True
    # If divisible by 2 or 3, not prime
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # Next prime
    i = 5
    # If i * i > n, no number above can be divided into n
    while i * i <= n:
        # Tests if n is divisible by i or i + 2
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # Only checking odd numbers that are not divisible by 3 (increased efficiency)
        i += 6
    return True

def nthPrime(n):
    """Function to find the nth prime number"""
    # 2 is the first prime
    if n == 1:
        return 2
    # Already accounted for n = 2, so count starts at 1
    count = 1
    # Only odd numbers, candiate = 1 then +=2
    candidate = 1
    
    while count < n:
        candidate += 2
        
        if prime_check(candidate):
            # Add to count if prime_check returns True
            count += 1
    return candidate