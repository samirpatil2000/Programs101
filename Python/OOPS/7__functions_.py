



sam=[]


class Employee:
    
    num_of_count=0
    raise_amt_value=10
    
    def __init__(self,name="Sam",amt=9) -> None:
        self.name=name
        self.amt=amt
        self.email=str(name)+"@gmail.com"
        Employee.num_of_count+=1
        
    def add_sam_function(self):
        sam.append(3)
        return {"Sam":sam.copy()}
        


class Manager(Employee):
    def add_sam_function(self):
        res=super().add_sam_function()
        sam.append(4)
        return res,sam

sol=Manager()
print(sol.add_sam_function())
    
