function specialPythagoreanTriplet(n) {
    var pythag = [];
    for (var a = 1; a < n; a++) {
      for (var b = a + 1; b < n; b++) {
        var c = n - a - b;
        if (a < b && b < c && (a*a + b*b) == c*c) {
          return a*b*c;
        }
      }
    }
    return -1;
  }
                    
        

specialPythagoreanTriplet(24)