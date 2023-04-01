function fiboEvenSum(n) {
    let fib_seq = [];
    let n1 = 0, n2 = 1;
  
    for (let i = 2; i < n; i++) {
      let n3 = n1 + n2;
      n1 = n2;
      n2 = n3;
      if (n3 <= n && n3 % 2 === 0) {
        fib_seq.push(n3);
      }
    }
    
    return fib_seq.reduce((acc, curr) => acc + curr, 0);
  }