import Car from './10-car.js';

class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(this._brand, this._motor, this._color);
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  get range() {
    return this._range;
  }
}

export default EVCar;
