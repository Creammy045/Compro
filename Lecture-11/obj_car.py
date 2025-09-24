class Car:
    #class attribute
    wheels = 4
    
    #Initializer method (constructor)
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    #Method
    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now running."
    
    #Method
    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is now off."
    
#Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
    
#Accessing instance attributes
print(my_car.make) #Output: Toyota
print(my_car.model) #Output: Corolla
print(my_car.year) #Output: 2020
    
#Calling instance methods
print(my_car.start_engine()) #Output: The engine of the 2020 Toyota Corolla is now running.
print(my_car.stop_engine()) #Output: The engine of the 2020 Toyota Corolla is now off.