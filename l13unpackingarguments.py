# => Unpacking Arguments

def sayhi(name, age):
    print(f'my name is {name}, i am {age} years old')


# => Unpacking positional Arguments
sayhi("Su Su", 30)

args = ("yu yu", 20)
sayhi(*args) # my name is yu yu, i am 20 years old


def addingnumbers(a, b, c):
    print(f"Sum Result = {a+b+c}")

addingnumbers(1,2,3) # 6

tuplenumbers = (10,20,30)
addingnumbers(*tuplenumbers)    # 60


listnumbers = [100,200,300]
addingnumbers(*listnumbers)    # 606


# => unpack keyword argument
listinfo = {"name": "Hla Hla", "age":30}
sayhi(**listinfo);