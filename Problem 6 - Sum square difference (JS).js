function sumSquareDifference(n) {
    const sumOfTheSquares = [...Array(n+1).keys()].slice(1).reduce((acc, val) => acc + val ** 2, 0);
    const squareOfTheSum = ([...Array(n+1).keys()].slice(1).reduce((acc, val) => acc + val, 0)) ** 2;
    const difference = squareOfTheSum - sumOfTheSquares;
    return difference;
  }