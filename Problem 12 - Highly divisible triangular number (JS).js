function divisibleTriangleNumber(n) {
    let triangle_numbers_factors = [];
    let i = 1;

    while (true) {
        // Generate the ith triangle number
        let integers = [];
        for (let j = 1; j < i; j++) {
            integers.push(j);
        }
        let triangle_number = integers.reduce((a, b) => a + b, 0);

        // Getting factors of each triangle number
        let factors = [];
        for (let j = 1; j <= Math.sqrt(triangle_number); j++) {
            if (triangle_number % j === 0) {
                factors.push(j);
                if (j !== triangle_number / j) {
                    factors.push(triangle_number / j);
                }
            }
        }

        // If number of factors >= n, solution found
        let number_of_factors = factors.length;
        if (number_of_factors >= n) {
            triangle_numbers_factors.push(factors);
            return triangle_number;
        }
        i++;
    }
}
divisibleTriangleNumber(500);