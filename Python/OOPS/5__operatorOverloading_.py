
class Employee:
    
    num_of_count=0
    
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        self.email=str(name)+"@gmail.com"
        Employee.num_of_count+=1
        
    def fullName(self):
        return "full name is {}".format(self.name)
    
    def __repr__(self) -> str:
        return "Employee('{}','{}')".format(self.name,self.amt)
    
    def __str__(self) -> str:
        return self.name
    
    def __add__(self,other):
        return self.amt+other.amt
        
    
    

emp=Employee("Samir1",400)
emp1=Employee("Samir2",300)

""" Both are the same """
print(repr(emp)) 
print(emp.__repr__()) 
print(str(emp))


""" Both are the same """
print(1+2)
print(int.__add__(1,2))


print(emp1+emp," or ", Employee.__add__(emp1,emp))