class Vehicle:
    default_fuel = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.default_fuel

    def drive(self, kilometers):
        fuel_cost = kilometers * self.fuel_consumption
        if fuel_cost <= self.fuel:
            self.fuel -= fuel_cost
