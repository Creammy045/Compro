from abc import ABC, abstractmethod

class employee(ABC):
    def emp_id(self, id, name, age, salary): #Abstraction
        pass
    
class childempyee1(employee):
    def emp_id(self, id):
        print("emp_id is 12345")
        
emp1 = childempyee1()
emp1.emp_id(id)