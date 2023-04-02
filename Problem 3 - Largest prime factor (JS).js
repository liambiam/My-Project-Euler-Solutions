function largestPrimeFactor(number) {
    const primeFactors = [];
  
    for (let num = 2; num <= number; num++) {
      let isPrime = true;
  
      for (let i = 2; i < num; i++) {
        if (num % i === 0) {
          isPrime = false;
          break;
        }
      }
  
      if (isPrime && number % num === 0) {
        primeFactors.push(num);
      }
    }
  
    return primeFactors[primeFactors.length - 1];
  }
  