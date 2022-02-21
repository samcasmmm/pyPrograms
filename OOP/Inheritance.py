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

    @staticmethod
    def print1(string):
        print('This is function ' + string)
        return 'Nothing'


class Programmer(Emp):
    def __init__(self, ename, esalary, erole, lang):
        self.name = ename
        self.salary = esalary
        self.role = erole
        self.lang = lang

    def printProgammer(self):
        return f'Programmer Name : {self.name} \n' \
               f'Programmer Salary : {self.salary}\n' \
               f'Programmer Role : {self.role}\n' \
               f'Programming Language : {self.lang}'


sam = Emp('sammer', 50000, 'CEO')
krimz = Emp('krimzz', 30000, 'Dev')
sameer = Programmer('SameerBagwan', 40000, 'Programmer', ['python', 'java'])
sahil =  Programmer('sahil', 35000, 'Programmer', ['Python'])
# print(f'{sam} \n{sameer} \n{krimz}')
print(sameer.printProgammer())