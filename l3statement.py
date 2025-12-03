if True:
    print("Yes")
else:
    print("No")



if False:
    print("Yes")
else:
    print("No")


if 5 == 5: #must be one space 5 == 5
    print("Yes")
else:
    print("No")


if 5 != 5: 
    print("Yes")
else:
    print("No")


if 5 > 1: 
    print("Yes")
else:
    print("No")


if 5 >= 5: 
    print("Yes")
else:
    print("No")


if 5 < 1: 
    print("Yes")
else:
    print("No")


if 5 <= 5:
    print("Yes")
else:
    print("No")




a = [10,20,30]
b = a 
c = [1000,2000,3000]


print(a is b) # True
print(a is c) # False
print(a is not c) # True




x = [10,20,30,40,50]
print(20 in x) # True
print(500 in x) # False


print("e" in "student") # True
print("o" not in "orange") # False

girls = ["su su","yu yu","nu nu"]
print("yu yu" in girls) # True
print("Yu Yu" in girls) # False
print("yu" in girls) # False






# => isinstance(val,type)

if isinstance("Hello",str):
    print("Yes")
else:
    print("No")


if isinstance(5,int):
    print("Yes")
else:
    print("No")


if isinstance(5.67,float):
    print("Yes")
else:
    print("No")


if isinstance(False,bool):
    print("Yes")
else:
    print("No")


if isinstance(["su su"],list):
    print("Yes")
else:
    print("No")


if isinstance({"name":"nu nu"},dict):
    print("Yes")
else:
    print("No")


# Nested if Statement

initnum = 25

if initnum > 0:
    print('The Init Number is positive')
    if initnum % 2 == 0:
        print("The Init Number is even")
    else:
        print("The Init Number is odd")
else:
    print('The Init Number is not positive')



# Ternary conditional operator
# true if condition else false


initidx = -10
result = "Positive Idx" if initidx > 0 else "Negative Idx"
print(result) # Positive Idx

result = "Even Idx" if initidx % 2 else "Odd Idx"
print(result) # Odd Idx

gamestatus = False
color = "Green Color" if gamestatus == True else "Red Color"
print(color) # Red Color


#Comparison Operators
# == Equal
# != Not Equal
# > Greater Than
# < Less Than
# >= Greater Than or Equal To 
# <= Less Than or Equal To 
# is , is not      Identity Operators 
# in , not in     Membership Operators







