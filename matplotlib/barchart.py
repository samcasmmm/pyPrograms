import matplotlib.pyplot as mp
x = ['Science', 'Commerce', 'Arts']
h = [200, 300, 500]
mp.bar(x, h)
mp.xlabel('Courses')
mp.ylabel('Student Enrolled')
mp.title('Student Enrolled for Different Courses')
mp.show()