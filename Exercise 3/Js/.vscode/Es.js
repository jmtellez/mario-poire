// change everything below to the newer Javascript!

// let + const
// Destructuring
class person{
  constructor( firstName, lastName, age, eyeColor, city ){
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.eyeColor = eyeColor;
    this.city = city;
  }
}

myperson = new person( "Mario", "Poire", 27, "Green", "mission" )

// Object properties
let a = 'test';
let b = true;
let c = 789;
a = 'test2';

const okObj = {
  a: a,
  b: b,
  c: c
};

console.log(Object.keys(okObj));

// Template strings
console.log('Hello ' + myperson.firstName + ' have I met you before? I think we met in ' + myperson.city + ' last summer no???');

// default arguments
// default age to 10;
let isValidAge = (age) => 10
console.log(isValidAge())

// Symbol
// Create a symbol: "This is my first Symbol"
sym1 = Symbol("this is my first symbol")

// Arrow functions
let whereAmI = (username, location) => (username && location) ? 'I am not lost' : 'I am totally lost!'
