
 ## 1.
# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled
# distance. Add a class initializer that sets the first two of the properties based on parameter values. The current
# speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create
# a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


# --- Main Program ---
car1 = Car("ABC-123", 142)

print("Car details:")
print("Registration number:", car1.registration_number)
print("Maximum speed:", car1.max_speed)
print("Current speed:", car1.current_speed)
print("Travelled distance:", car1.travelled_distance)


## 2..
# Extend the program by adding an accelerate method into the new class. The method should receive the change of speed
# (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the
#  speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
#  Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally
#  +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h
#  change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print("Current speed after accelerating:", car1.current_speed)

car1.accelerate(-200)
print("Final speed after braking:", car1.current_speed)


### 3.
# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given
# time. Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call
# car.drive(1.5) increases the travelled distance to 2090 km.

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car1 = Car("ABC-123", 142)
car1.accelerate(60)
car1.drive(1.5)
print("Travelled distance:", car1.travelled_distance, "km")



### 4.
# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning
# of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed
# of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as
# follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following
# operations are performed:
#     The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
#     This is done using the accerelate method.
#     Each car is made to drive for one hour. This is done with the drive method


import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


cars = []

for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_num, max_speed))

race_over = False

while not race_over:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_over = True

print("Race finished! Final distances:")
for car in cars:
    print(f"{car.registration_number}: {car.travelled_distance:.1f} km, Max Speed: {car.max_speed} km/h")





































































































