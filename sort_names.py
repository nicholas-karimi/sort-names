
class Employee:
    def __init__(self, name, department, designation, salary):
        self.name = name 
        self.department = department
        self.designation = designation
        self.salary = salary


    def __repr__(self):
        return repr((self.name, self.department, self.designation, self.salary))



#Instantiate class 
employee = [
        Employee('Nicolas Karimi', 'ICT', 'Software Developer', '$600'),
        Employee('Lucy Kaki', 'Procurement', 'Procurement Officer', '$700'),
        Employee('Ann Muchoki', 'Sales & Marketing', 'Lead Officer', '$340'),
        ]

print(sorted(employee, key=lambda employee: employee.name))
