const s = "func &&";
const newString = s.replace(/&/g, "");
console.log(newString); // Output: "func "

const s = "sad".split("").reverse().join("")