def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multipy(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

while True:
    userinput = input("Enter choice 1/2/3/4: ")

    if userinput in ("1","2","3","4"):
        firstnum = float(input("First num: "))
        secondnum = float(input("Second num: "))

        if userinput == "1":
            result = add(firstnum, secondnum)
            print(f"{firstnum} + {secondnum} = {result}")
        elif userinput == "2":
            result = sub(firstnum, secondnum)
            print(f"{firstnum} - {secondnum} = {result}")
        elif userinput == "3":
            result = multipy(firstnum, secondnum)
            print(f"{firstnum} * {secondnum} = {result}")
        elif userinput == "4":
            result = divide(firstnum, secondnum)
            print(f"{firstnum} / {secondnum} = {result}")

        nextcal = input("Do you want to play again: Yes or No: ").lower()
        if nextcal == "no":
            print("Bye Bye!")
            break
    else:
        print("Invalid Input")


