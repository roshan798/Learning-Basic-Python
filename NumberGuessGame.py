import random

NUM = random.randint(0, 100)
flag = False
print("Guess the number (0-100)")
score = 0
while not flag:
    score += 1
    x = int(input("Enter the number: "))
    if x == NUM:
        print("You Won!!!")
        print("Your Rank: " + str(score))
        flag = True
    elif x > NUM:
        print("Enter a smaller number")
    else:
        print("Enter a greater number")
