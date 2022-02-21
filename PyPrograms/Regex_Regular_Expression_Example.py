# regex regular expression


import re

txt = "Hello World Good morn"
x = re.search("^Hello.*morn$", txt)

if x:
    print("Match")
else:
    print("No Match")

x = re.findall("Good", txt)
print(x)

# #^ Carrat text should start with this
# #.* its has many characters after it
# #$ it is ending with this string
