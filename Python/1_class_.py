class Employee:
    no_of_leaves = 8

    def _init_(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


Amar = Employee("Amar", 600, "Developer")
print(Amar.salary)