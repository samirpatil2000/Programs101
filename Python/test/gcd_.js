function gcd(a, b) {
    if (b > a) {
      [a, b] = [b, a];
    }
  
    while (b !== 0) {
      let remainder = a % b;
      a = b;
      b = remainder;
    }
    return a;
  }
  
  // Example usage:
  let number1 = 12;
  let number2 = 13;
  let result = gcd(number1, number2);
  console.log(result); // Output: 12
  