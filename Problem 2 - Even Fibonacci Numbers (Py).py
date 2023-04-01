def fiboEvenSum(n):
    
    fib_seq = []
    
    n1, n2 = 0, 1

    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n3 <= n and n3 % 2 == 0:
            fib_seq.append(n3)
    
    return sum(fib_seq)

   

fiboEvenSum(1000)