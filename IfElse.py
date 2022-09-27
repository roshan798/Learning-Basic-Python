def can_vote(age):
    if age < 18:
        return "NO"
    else:
        return "YES"


age = input("Enter your age: ")
print("you can vote or not: " + can_vote(int(age)))
