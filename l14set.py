# => Data Containers

#list
mylist = [1,2,3,4,5]
print(type(mylist))  # class= list


#tuple
mytuple = (1,2,3,4,5)
print(type(mytuple))  # class= tuple


#dict
mydict = {"a":1, "b":2, "c": 3}
print(type(mydict))  # class= tuple


#set
myset = {1,2,3,4,5}
print(myset)            # {1,2,3,4,5}
print(type(myset))      # set



dict1 = {}
print(type(dict1)) # dict


set1 = {}
print(type(set1)) # dict

#create an empty set
set2 = set()
print(type(set2))  # set


colors = {"red","green","blue","whiet","black"}
print(colors)
print(type(colors))

for color in colors:
    print(color)

print("green" in colors) # True
print("steelblue" in colors) # False


