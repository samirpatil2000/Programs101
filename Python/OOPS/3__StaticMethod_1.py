class Employee:
    num_of_count=0
    raise_amt=1.04
    def __init__(self,name,amt) -> None:
        self.name=name
        self.amt=amt
        Employee.num_of_count+=1
        
    @staticmethod
    def is_Hollyday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return True
        return False
    @staticmethod
    def return_count_pre():
        return Employee.num_of_count*100
        
    
import datetime
my_date=datetime.date(year=2021,month=6,day=20)
print(Employee.is_Hollyday(my_date))
print(Employee.return_count_pre())
e=Employee("Sa",1)
print(e.name,e.amt)

e=Employee("Sa",1)
print(e.name,e.amt)

e=Employee("Sa",1)
print(e.name,e.amt)
print(Employee.return_count_pre())
