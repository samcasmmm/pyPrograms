# # Ques 1

# tup = (1, 2, 3, 4, 5, 2, 2, 12)
# print("Count :", tup.count(2))
# print("Index :", tup.index(12))

# # Ques 2
#
# odd = []
# even = []
# for i in range(1, 51):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#
# print("Even Numbers = ", even)
# print("Odd Numbers = ", odd)
#
# # Ques 3
#
# list1 = [10, 3, 4, 8, 9, 6]
# list2 = [7, 2, 5, 1]
#
# list1.append(888)
# print("Append :", list1)
#
# list1.extend(list2)
# print("Extend :", list1)
#
# list1.insert(2, 333)
# print("Insert :", list1)
#
# print("Index :", list1.index(5))
#
# list1.sort()
# print("Sorted :", list1)
#
# # Ques 4
#
# file = open("Example.txt", 'r')
# print(file.readline())
# print(file.readline())
# file.close()
#
#
# # Ques 5
#
# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#
#     def display(self):
#         print("Student Name :", self.name)
#         print("Student Roll No :", self.rollno)
#         print("Student Age :", self.Age, "and Total Marks :", self.Marks)
#
#     def setAge(self):
#         self.Age = int(input("Enter your Age "))
#
#     def setMarks(self):
#         self.Marks = int(input("Enter the Total Marks "))
#
#
# s1 = Student("Sameer", 101)  # creating Obj
#
# s1.setAge()
# s1.setMarks()
# s1.display()
#
# # Ques 6
#
# import datetime
#
# print("Current Date and Time :", datetime.datetime.now())
# print("Current Year :", datetime.date.today().strftime("%Y"))
# print("Month of year :", datetime.date.today().strftime("%B"))
# print("Week number of the year :", datetime.date.today().strftime("%W"))
# print("Weekday of the week :", datetime.date.today().strftime("%A"))
#
#
# # Ques 7
#
# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def isEmployee(self):
#         return "Not Employed"
#
#
# class Employee(Person):
#
#     def isEmployee(self):
#         return "Employed"
#
#
# emp = Person("Sameer")
# print('Employee Name :', emp.name)
# print('Employment Status :', emp.isEmployee())
#
# emp = Employee("Sam")
# print('Employee Name :', emp.getName())
# print('Employment Status :', emp.isEmployee())


#
# # Ques 8
#
# num = int(input("Enter the Number "))
# for i in range(1, 11):
#     print(f'{num} * {i} = {num*i}')
#
#
# # Ques 9
#
# def showEmp(name, salary=5000):
#     print("Employee Name :", name)
#     print("Employee Salary :", salary)
#
# showEmp("Sam")
# showEmp("Sameer", 40000)
#
# # Ques 10
#
# num = int(input("Enter the Number : "))
# div = []
# a = ([i for i in range(1, num + 1) if not num % i])
# div.append(a)
# print("Divisors :", div)
