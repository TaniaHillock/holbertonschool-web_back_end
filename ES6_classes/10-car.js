const _brand = Symbol('brand');
const _motor = Symbol('motor');
const _color = Symbol('color');

class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  someMethod() {
    console.log(this._brand);
  }    
  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }
}

export default Car;
