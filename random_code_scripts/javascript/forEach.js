radii = [1, 5, 2, 9];

const getArea = (radius) => Math.PI * radius ** 2;
const getCircumference = (radius) => 2 * Math.PI * radius;
const getDiameter = (radius) => 2 * radius;

radii.forEach(radius => console.log(`The area of a circle of radius ${radius} is ${getArea(radius)}, circumference is ${getCircumference(radius)} and the diameter is ${getDiameter(radius)}`));

