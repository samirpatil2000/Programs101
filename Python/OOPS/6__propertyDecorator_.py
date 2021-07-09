
class Employee:
    
    num_of_count=0
    
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
    
    # this help you method as attributes 
    @property
    def email(self):
        return str(self.name)+"@gmail.com"   
     
    @property  
    def fullName(self):
        return "The FullName is {}".format(self.name)
    
    # @fullName.setter
    # def function(self,name):
    #     return str(name)
        
    
    

emp1=Employee("Samir",300)


print(emp1.name,emp1.email)
print(emp1.fullName)

emp1.name="Sam"
print("\n")

print(emp1.name,emp1.email)
print(emp1.fullName)


# now it will through error you can't set property method directly
# emp1.fullName="a"

