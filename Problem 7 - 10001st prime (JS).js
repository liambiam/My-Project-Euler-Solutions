function primeCheck(n) {
    if (n <= 1) {
      return false;
    } else if (n <= 3) {
      return true;
    } else if (n % 2 == 0 || n % 3 == 0) {
      return false;
    }
    let i = 5;
    while (i * i <= n) {
      if (n % i == 0 || n % (i + 2) == 0) {
        return false;
      }
      i += 6;
    }
    return true;
  }
  
  function nthPrime(n) {
    if (n == 1) {
      return 2;
    }
    let count = 1;
    let candidate = 1;
    while (count < n) {
      candidate += 2;
      if (primeCheck(candidate)) {
        count += 1;
      }
    }
    return candidate;
  }