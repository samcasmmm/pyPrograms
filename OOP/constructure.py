class Emp:
    Num_of_emp = 10

    def __init__(self, ename, esalary, erole, ):
        self.name = ename
        self.salary = esalary
        self.role = erole

    def showDetails(self):
        return f'Employee Name : {self.name} \n' \
               f'Employee Salary : {self.salary}\n' \
               f'Employee Role : {self.role}'

    @classmethod
    def changeNo(cls, NewEmp):  # CLASSMETHOD TAKE cls insttead of self
        cls.Num_of_emp = NewEmp  # change class variable

    @classmethod
    def from_str(cls, sting):
        params = sting.split(' ')
        return params
        # return cls(*sting.split(' '))

# employee1 = Emp('sameer', 400000, 'HR')
# employee1.changeNo(21)
# print(employee1.Num_of_emp)
# employee1.Num_of_emp+=1
# print(employee1.Num_of_emp)
# print(employee1.showDetails())


sam = Emp.from_str('sam 50000 Dev')
print(sam)
