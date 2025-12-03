
# Function 
# 1. Simple Function with No Parameters
# 2. Function with Parameter 
#         (i) Single Parameter Funciton 
#         (ii) Multi Parameter Function 
# 3. Function with Default Parameter
# 4. Function with a Return Value 
# 5. Function with multi Return Values
# 6. Lambda Function ( Anonymous Function )



def sayname():
    print("Hello Aung Aung")

sayname()
sayname()


# 2. Function with Parameter
#           (i) Single Parameter Function


def saycity(city):
    print("Hello" + city)

saycity("Yangon")
saycity("Mandalay")




# 3. Function with Default Parameter

def country(country="Thailand"):
    print( f"Hello {country}" )

country()
country("Myanmar")
country("Indonesia")




# 4. Function with Return Value

def sayage():
    return "I am 25 year old"

print(sayage())


def saynickname():
    result = "Daw Pu"
    return result

print(saynickname())


def saynum(num1=20):
    return num1 

print(saynum(100))
print(saynum())



def greeting(value="yamin"):
    return f"Hello {value}"

print(greeting("Su Su"))
print(greeting())



def funone(num1,num2):
    result = num1+num2  
    return result


print(funone(10,30))



def funtwo(num1,num2=200):
    result = num1+num2  
    return f"Total value is = {result}"


print(funtwo(10))
print(funtwo(10,20))



# 5. Function with multi Return Values

def saynameandage():
    name = 'Honey'
    age = 26
    city = "Yangon"
    return name,age,city


print(saynameandage())  #('Honey', 26, 'Yangon')

name,age,city = saynameandage()
print(name) # Honey
print(age) # 26
print(city) # Yangon




# 6. Lambda Function ( Anonymous Function )

addresult = lambda num1,num2,num3:num1+num2+num3 
print(addresult(200,300,400))


sumresult = lambda num1,num2=200,num3=500:num1+num2+num3 
print(sumresult(200,300))
print(sumresult(100))



# inputval = input("Enter your name = ")
# msg = "Hello "+inputval
# msg = "Hello %s" % inputval  #v2 (do not use)
# msg = f"Hello {inputval}" #v3
# print(msg)


firstname = input("Enter First Name = ")
lastname = input("Enter Last Name = ")
# fullname = "Hello %s%s" % (firstname,lastname) #v2
# fullname = "Hello %s %s" % (firstname,lastname) #v2
fullname = f"Hello {firstname} {lastname}" #v3
print(fullname)