num1 = 256.99
print(int(num1)) # 256

num2 = "528"
print(int(num2)) # 528

# num3 = "1500.56"
# print(int(num3)) # ValueError

num4 = 100
print(abs(num4)) # 100

num5 = -200
print(abs(num5)) # 200


num6 = "3.67"
print(float(num6)) # 3.67

num7 = 5
print(float(num7)) # 5.0

num8 = 4.586862
print(round(num8)) # 5
print(round(num8,1)) # 4.6
print(round(num8,2)) # 4.59
print(round(num8,3)) # 4.587


# (2^3 = 8)
print(pow(2,3)) # 6
print(pow(2,5)) # 32

# 10//2 = 5 , 10%2 = 0
print(divmod(10,2)) # (5,0)
print(divmod(9,2)) # (4,1)
print(divmod(100,3)) # (33,1)

print(max(10,50,20,18,30)) # 50
print(min(10,50,20,18,30)) # 10

print(sum([1,2,3,4,5])) # 15
print(sum((1,2,3,4,5))) # 15

# Mathematical Functions (from math module)
# To use the math module ! you need to import

import math 

print(math.pow(3,2)) # 8.0
print(math.pow(3,3)) # 27.0

print(math.sqrt(16)) # 4.0
print(math.sqrt(64)) # 8.0
print(math.sqrt(36)) # 6.0
print(math.sqrt(35)) # 5.916079783099616

print(math.ceil(3.2)) # 4
print(math.ceil(3.5)) # 4
print(math.ceil(3.0)) # 3

print(math.floor(3.2)) # 3
print(math.floor(3.7)) # 3


# e (Euler number) is approximately
print(math.e) # 2.718281828459045


print(math.log(100,10)) # 2.0 (log base 10)
print(math.log(81,9)) # 2.0 (log base 9)

print(math.log(10,2)) # 3.3219280948873626
print(math.log(100,2)) # 6.643856189774725

# default is e
print(math.log(100)) # 4.605170185988092


print(math.log10(100)) # 2.0 (log base 10)
print(math.log10(1000)) # 3.0 (log base 10)


print(math.log2(8)) # 3.0



# math.exp(exponential)
print(pow(2.718281828459045,2)) # 7.3890560989306495
print(math.exp(2)) # 7.38905609893065

print(pow(2.718281828459045,3)) # 20.085536923187664
print(math.exp(3)) # 20.085536923187668


import random 

print(random.random()) # 0.5302771776062997
print(random.random()) # 0.7375208441820552


print(random.randint(1,10)) # return a integer between x,y

print(random.uniform(1.5,4.5)) # return a float between x,y ,  1.691194776231761

numlists = [10,200,300,400,5000]
print(random.choice(numlists)) # random element from the list

numtuple1s = (10,200,300,400,5000)
print(random.choice(numtuple1s)) # random element from the list

numtuple2s = 10,200,300,400,5000
print(random.choice(numtuple2s)) # random element from the list

