def largestPalindromeProduct(n):

    number = int("9" * n)
    palindromes = []

    for i in range(1,number + 1):
        for j in range(1,number + 1):         
            m = str(i * j)        
            if m == m[::-1]:           
                palindromes.append(int(m))
    palindromes.sort()
    return palindromes[-1]

largestPalindromeProduct(3)


                
    
