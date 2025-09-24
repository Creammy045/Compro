class Animal:
    def __init__(self, name):
        self.name = name
        
    def spesk(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
    
#Creating objects of child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak()) #Output: Buddy says woof!
print(cat.speak()) #Output: Whiskers says meow!