### 1..
# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator
# has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h
# for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times
# as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator
# is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice
# and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        print(f"Moving from floor {self.current_floor} to floor {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")


h = Elevator(1, 10)
h.go_to_floor(5)
h.go_to_floor(1)




### 2..
# Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of
# the bottom and top floors and the number of elevators in the building. When a building is created, the building creates
# the required number of elevators. The list of elevators is stored as a property of the building. Write a method called
# run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program,
# write the statements for creating a new building and running the elevators of the building.


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        print(f"Elevator moving from {self.current_floor} to {target_floor}")
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Now on floor {self.current_floor}")
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Now on floor {self.current_floor}")
        print(f"Reached floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        if 0 <= elevator_number < len(self.elevators):
            print(f"\nRunning elevator {elevator_number + 1}")
            self.elevators[elevator_number].go_to_floor(target_floor)
        else:
            print("Invalid elevator number!")


building = Building(1, 10, 2)
building.run_elevator(0, 5)
building.run_elevator(1, 8)




### 3.
# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to
# the bottom floor. Continue the main program by causing a fire alarm in your building.


class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            print(f"Elevator now on floor {self.current_floor}")
        while self.current_floor > target_floor:
            self.current_floor -= 1
            print(f"Elevator now on floor {self.current_floor}")
        print(f"Elevator reached floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        self.bottom_floor = bottom_floor

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nElevator {elevator_number + 1} running...")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n🚨 Fire alarm! All elevators returning to bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i + 1} returning to floor {self.bottom_floor}")
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 3)
building.run_elevator(0, 6)
building.run_elevator(1, 8)
building.fire_alarm()



### 4.

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<10}{'Speed(km/h)':<15}{'Distance(km)':<15}")
        print("-" * 40)
        for car in self.cars:
            print(f"{car.registration_number:<10}{car.current_speed:<15}{car.travelled_distance:<15.1f}")

    def race_finished(self):
        return any(car.travelled_distance >= self.distance for car in self.cars)


cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"\n--- Hour {hours} ---")
        race.print_status()

print("\n🏁 Race finished! Final results:")
race.print_status()




























































































































