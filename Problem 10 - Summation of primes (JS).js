function primeSummation(n) {
  var is_prime = [];
  var prime_sum = 0;

  // Initialize the array with true values for all numbers
  for (var i = 0; i < n; i++) {
      is_prime.push(true);
  }

  // Set multiples of primes to false
  for (var i = 2; i * i < n; i++) {
      if (is_prime[i]) {
          for (var j = i * i; j < n; j += i) {
              is_prime[j] = false;
          }
      }
  }

  // Add up all prime numbers
  for (var i = 2; i < n; i++) {
      if (is_prime[i]) {
          prime_sum += i;
      }
  }

  return prime_sum;
}