# Reading from a file
"""
file = open("text.txt", 'r')
# print(file.read())
# line = file.readline()  # reading one line
# print(line)
lines =  file.readines()
for line in lines:  # printing line by line
    print(line)
# print(lines)
"""

# Writing into file
"""
file = open("text1.txt", "w")
file.write("Hello I am roshan\n")
file.write("I am learning python")
file.writelines("\n"+input("Enter text: "))
"""
"""
# appending to file
file = open("text2.txt", "a")
if file.writable():
    file.write("\n"+input("Enter some text: "))
else:
    print("File not exist")

"""



