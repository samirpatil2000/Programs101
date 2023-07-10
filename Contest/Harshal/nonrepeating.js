function areDistinct(str, start, end) {
    const visited = new Array(26).fill(false);
  
    for (let i = start; i <= end; i++) {
      const charIndex = str.charCodeAt(i) - 'a'.charCodeAt(0);
      if (visited[charIndex]) {
        return false;
      }
      visited[charIndex] = true;
    }
    return true;
  }
  
  function longestNonRepeating(str) {
    const n = str.length;
    let longestSubstring = "";
  
    for (let i = 0; i < n; i++) {
      for (let j = i; j < n; j++) {
        if (areDistinct(str, i, j)) {
          const currentSubstring = str.substring(i, j + 1);
          if (currentSubstring.length > longestSubstring.length) {
            longestSubstring = currentSubstring;
          }
        }
      }
    }
  
    return longestSubstring;
  }
  
  // Example usage:
  const string = "abcabcbb";
  const result = longestNonRepeating(string);
  console.log(result); // Output: "abc"
  