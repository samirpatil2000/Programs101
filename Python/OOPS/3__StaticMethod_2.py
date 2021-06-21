class Employee:
    num_of_count=0
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        Employee.num_of_count+=1
        
    "throws error"
    # def passIngInstance(e:Employee):
    #     pass
    
class MyClass:
    
    @staticmethod
    def increamentSalary(e:Employee):
        e.name=["sa"]
        e.amt+=100





        
    
        
    

e=Employee("Sa",1)
print(e.name,e.amt)

# print(Employee.return_count_pre())
MyClass.increamentSalary(e)
print(e.name,e.amt)
