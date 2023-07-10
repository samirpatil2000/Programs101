function isPrime(number) {
    if (number <= 1) {
      return false;
    }
    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false;
      }
    }
      return true;
  }
  
  // Example usage:
  let number = 39;
  let result = isPrime(number);
  console.log(result);
  