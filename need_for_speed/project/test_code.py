from need_for_speed.project.vehicle import Vehicle
from need_for_speed.project.car import Car

vehicle = Vehicle(50, 150)
print(Vehicle.default_fuel)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = Car(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)