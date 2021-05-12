// change everything below to the newer Javascript!

// let + const
let a = 'test';
const b = true;
const c = 789;
a = 'test2';

// Destructuring
const person = {
  firstName : "John",
  lastName  : "Doe",
  age       : 50,
  eyeColor  : "blue",
  city      : "Houston"
};

const { firstname, lastname, age, eyeColor, city } = person;

// Object properties

const okObj = {a:'a', b: 'b', c: 'c'}

console.log(Object.keys(okObj));

// Template strings
let greeting = `Hello ${person.firstName} have I met you before? I think we met in ${person.city} last summer no???`
console.log(greeting);

// default arguments
// default age to 10;
function isValidAge(age = 10) {
  return age
}
console.log(isValidAge());

// Symbol
// Create a symbol: "This is my first Symbol"
sym1 = Symbol("this is my first symbol")

// Arrow functions
let whereAmI = (username, location) => (username && location) ? 'I am not lost' : 'I am totally lost!'
