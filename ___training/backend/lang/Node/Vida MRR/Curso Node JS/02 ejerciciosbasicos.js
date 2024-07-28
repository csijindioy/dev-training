console.log("Hola mundo");

var path = require("path");

var a = 5;
var b = 10;

console.log("El resultado es " + (5 + 10))
console.log(`El resultado es ${a + b}`)
console.log(`El resultado es ${a == b}`)

console.log(__dirname);
console.log(__filename);

console.log(path.basename(__filename))

