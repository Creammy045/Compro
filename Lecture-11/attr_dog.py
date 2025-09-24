class Dog:
    #Class Attribute
    spcies = 'mammal'
    
    #Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the dog object        
dog1 = Dog("Philo", 5)
dog2 = Dog("Mikey", 6)

#Access the instance attributes
print("{} is {} and {} is {}."
.format(dog1.name, dog1.age, dog2.name, dog2.age))

#Is Phili a mammal?
if dog1.spcies == "mammal":
    print("{} is a {}!".format(dog1.name, dog1.spcies))