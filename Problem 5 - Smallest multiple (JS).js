function gcd(a, b) {
    if (b === 0) {
      return a;
    }
    return gcd(b, a % b);
  }
  
  function lcm(a, b) {
    return (a * b) / gcd(a, b);
  }
  
  function smallestMult(n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
      result = lcm(result, i);
    }
    return result;
  }