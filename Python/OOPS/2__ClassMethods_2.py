class Employee:
    num_of_count=0
    raise_amt=1.04
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        Employee.num_of_count+=1
        
    @classmethod
    def fromString(cls,str_:str):
        name,amt=str_.split("-")
        return cls(name.title(),amt)
    
    
e=Employee("Sa",1)
e1=Employee.fromString("samir-34")
e2=Employee.fromString("sam-35")

        
print(e.name,e.amt)
print(e1.name,e1.amt)
print(e2.name,e2.amt)
