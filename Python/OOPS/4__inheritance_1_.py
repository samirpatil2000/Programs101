

class Employee:
    
    num_of_count=0
    
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        self.email=str(name)+"@gmail.com"
        Employee.num_of_count+=1
        
    def fullName(self):
        return "full name is {}".format(self.name)
    
    def raise_amt(self):
        self.amt*=10
        return
    
class Developer(Employee):
    pass


class Manager:
    pass


dev=Developer("Samir",324)
dev2=Developer("Sami2r",324)
    
print(dev.amt)
dev.raise_amt()
print(dev.amt)




        
    
        
    

e=Employee("Sa",1)
print(e.name,e.amt)

