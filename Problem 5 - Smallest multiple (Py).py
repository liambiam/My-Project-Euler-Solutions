def gcd(a, b):
   if b == 0:
      return a
   return gcd(b, a % b)

def lcm(a, b):
   return (a * b) // gcd(a, b)

def smallestMult(n):
   result = 1
   for i in range(1, n+1):
      result = lcm(result, i)
   return result


smallestMult(5)