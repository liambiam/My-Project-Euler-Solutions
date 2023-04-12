def specialPythagoreanTriplet(n):

    pythag = []
    pythago = []

    for a in range(n+1):
        for b in range(n+1):
            for c in range (n+1):
                if a < b < c and (a + b + c) == n and (a**2 + b **2) == c**2:
                    pythag.append(a*b*c)
                    pythago.append(f"{a} {b} {c}")
                    
    
    print((pythag))
    print(pythago)
        
        

specialPythagoreanTriplet(24)