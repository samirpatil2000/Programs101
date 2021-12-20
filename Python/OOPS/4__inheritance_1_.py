

class Employee:
    
    num_of_count=0
    raise_amt_value=10
    
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        self.email=str(name)+"@gmail.com"
        Employee.num_of_count+=1
        
    def fullName(self):
        info={}
        info["x"]="full name is {}".format(self.name)
        return info
    
    def raise_amt(self):
        self.amt*=self.raise_amt_value
        return
    
    
class Developer(Employee):
    raise_amt_value=20
    
    def __init__(self, name,prog_lang) -> None:
        super().__init__(name,amt=None)
        self.prog_lang=prog_lang
    
    def fullName(self):
        return super().fullName()

class Manager(Employee):
    
    def __init__(self, name, amt,listOfEmployees) -> None:
        super().__init__(name, amt)
        self.email='{}@maganer.com'.format(self.name)
        if listOfEmployees:
            self.employees=listOfEmployees
        else:
            self.employees=[]
    
    def add_employes(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employes(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def printEmployees(self):
        for e in self.employees:
            print('--->',e.email)
    

            



emp=Employee("Samir1",324)
emp2=Employee("Samir2",324)
dev=Developer("Sami2r",prog_lang="Python")
    
# print(emp.amt,emp.raise_amt(),emp.amt)

# print(dev.email,dev.prog_lang,dev.amt)
"""
m1=Manager("SamirM",342,[emp])
print(m1.email)
m1.printEmployees()
m1.add_employes(emp2)
m1.printEmployees()"""





# print(isinstance(2,int))
# print(isinstance(emp,Employee))
# print(isinstance(emp,Developer)) # this returns false 

# print(issubclass(Developer,Employee))
# print(issubclass(Manager,Employee)) # this Returns True

class A(Employee):
    def __init__(self, name, amt,request) -> None:
        super().__init__(name, amt)
        self.name=name+"@"
        self.re=request
    

obj=A("Samir",23,request="Hello")
print(obj.name,obj.amt,obj.re)

print(0 or 1)
