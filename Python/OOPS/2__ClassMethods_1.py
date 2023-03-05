class Employee:
    num_of_count=0
    raise_amt=1.04
    
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        Employee.num_of_count+=1
    
    print("Hello X")
    def no(self):
        self.s=0
        return self.s
        
    @classmethod
    def set_amt(cls,amt):
        cls.raise_amt=amt
        
        
# e1=Employee("Samir",34)
# e2=Employee("Sam",35)

# print(Employee.raise_amt)
# print(e1.raise_amt)
# print(e2.raise_amt)


# """ Class Method """
# Employee.set_amt(1.05)
# """   OR  """

# # e1.set_amt(1.05)
        
# print(Employee.raise_amt)
# print(e1.raise_amt)
# print(e2.raise_amt)

# print(e1.no())