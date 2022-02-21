# class student:
#     def __init__(self, roll, name):  # to initialize roll and name
#         self.roll = roll
#         self.name = name
#
#     def display(self):  # i.to display student 's information
#         print(self.roll, self.name, self.age, self.marks)
#
#     def setAge(self):  # ii.to set age of the student
#         self.age = int(input("Enter age : "))
#
#     def setMarks(self):  # iii.to set marks of the student
#         self.marks = int(input("Enter marks : "))
#
#
# s1 = student(111, "Madhuri")  # creating objects
# s2 = student(222, "Tara")
# # calling methods
# s1.setAge()
# s1.setMarks()
# s2.setAge()
# s2.setMarks()
# s1.display()
# s2.display()

# num = int(input("Enter an Number : "))
# div = []
# for i in range(1, num + 1):
#     if num % i == 0:
#         div.append(i)
# print("Divisors of", num, "is :", div)


# import datetime
#
# age = datetime.datetime(2000, 5, 6).year
# today = datetime.datetime.now().year
# print(today - age)


# n = int(input())

# if n % 2 != 0:
#     print('weird')
# if n % 2 == 0 and n in range(2, 5):
#     print("not weird")
# if n % 2 == 0 and n in range(6, 20):
#     print("weird")
# if n % 2 == 0 and n > 20:
#     print("not weird")
