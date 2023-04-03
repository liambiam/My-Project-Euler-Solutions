function largestPalindromeProduct(n) {
    const number = parseInt("9".repeat(n));
    const palindromes = [];
    
    for (let i = 1; i <= number; i++) {
    for (let j = 1; j <= number; j++) {
    const m = (i * j).toString();
    if (m === m.split("").reverse().join("")) {
    palindromes.push(parseInt(m));
    }
    }
    }
    palindromes.sort((a, b) => a - b);
    return palindromes[palindromes.length - 1];
    }
    
    largestPalindromeProduct(3);
    