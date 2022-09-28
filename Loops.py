from math import floor

# iterative binary search


def binary_search(arr, key):
    lo = 0
    hi = len(arr)-1
    print(hi)
    while lo < hi:
        mid = floor((hi + lo) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

#  for each loop in python

# list = ['dfd', 'see we', 'sewer', 'perf']
# for x in list:
#     print(x)
# # while loop
# # printing table of
# n = int(input("Enter a number to print its table"))
# for i in range(1, 11):
#     print(n * i)
array = [3, 6, 3, 9, 7, 5, 3, 6, 6, 4, 543, 356, 432, 765, 4]
array.sort()
print(binary_search(array, 3))
