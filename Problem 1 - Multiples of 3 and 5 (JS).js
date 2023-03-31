function multiplesOf3and5(number) {
    const three_div = Math.floor((number - (number % 3)) / 3) + 1;
    const five_div = Math.floor((number - (number % 5)) / 5) + 1;
    const threes_fives = [];
    for (let i = 0; i < three_div; i++) {
        if (3 * i < number) {
            threes_fives.push(3 * i);
        }
    }
    for (let i = 0; i < five_div; i++) {
        if (5 * i < number) {
            threes_fives.push(5 * i);
        }
    }
    const distinct_threes_fives = [...new Set(threes_fives)];
    const sum = distinct_threes_fives.reduce((acc, curr) => acc + curr, 0);
    return sum;
}