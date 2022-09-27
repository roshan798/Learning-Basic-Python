# friends = ['karan', 'Rahul', 'Shivnath']  # list of string
# print(friends)  # printing all list elements
# # printing list by their indexes
# # when accessing element by positive index indexing starts from 0
# print(friends[0])
# # when accessing element by negative index indexing starts from -1
# print(friends[-1])
# print(friends[1])
# Roshan = ['Roshan', 19, 5.9, 'M']
# #  printing only two  elements
# print(Roshan[0:2])
# Roshan[3]='m'
# print(Roshan)
#
from typing import List, Union

Fruits: list[Union[str, int]] =['Apple', 'Banana', 'Lichi']
Lucky_numbers = [7, 2, 8, 4, 2]
# concatenating two lists
Fruits.extend(Lucky_numbers)
# print(Fruits)
print(Lucky_numbers)
# adding item into end of the list
Fruits.append("Mango")
Fruits.insert(3,'Mango')  # inserting mango at position 4

Fruits.remove('Lichi')  # removing an element

print(Fruits)
# deleting all values
# Fruits.pop()# deleting last value
# print((Fruits.index("Mango")))
# print((Fruits.count("Mango")))
# print(Fruits)
# Lucky_numbers.clear()
# print(Lucky_numbers)
Lucky_numbers.sort()
print(Lucky_numbers)
F2: list[Union[str, int]] = Fruits.copy()
print(F2)


