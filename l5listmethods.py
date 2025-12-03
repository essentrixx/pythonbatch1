names = ["aung aung","maung maung","su su","yu yu","nandar"]
print(names) # ['aung aung', 'maung maung', 'su su', 'yu yu', 'nandar']

mixeds = [1500,"hello",123.6,True,"world",False]
print(mixeds) #[1500, 'hello', 123.6, True, 'world', False]

print(mixeds[0]) # 1500
print(mixeds[3]) # True
print(mixeds[-1]) # False
print(mixeds[-2]) # world

print(mixeds[0:1]) # [1500]
print(mixeds[0:2]) # [1500, 'hello']
print(mixeds[1:3]) # ['hello', 123.6]
print(mixeds[0:6]) # [1500, 'hello', 123.6, True, 'world', False]

#start:end:step 
print(mixeds[0:6:2]) # [1500, 123.6, 'world']
print(mixeds[0:6:3]) # [1500, True]


mix2 = mixeds # [1500, 'hello', 123.6, True, 'world', False]
mix2 = mixeds[:] # [1500, 'hello', 123.6, True, 'world', False]
mix2 = mixeds[0:4] # [1500, 'hello', 123.6, True]
mix2 = mixeds[::-1] # [False, 'world', True, 123.6, 'hello', 1500]
print(mix2)

getlength = len(names)
print(getlength) # 5




colors = ["red","green","blue"]
print(colors) # ['red', 'green', 'blue']

# colors[3] = "silver" #error
# print(colors)

colors[0] = "pink"
print(colors) # ['pink', 'green', 'blue']


#add data from end (single)
colors.append("white")
#colors.append("black","violet") # error
print(colors) # ['pink', 'green', 'blue', 'white']


#add data from end (multi)
colors.extend(["gold"]) # ['pink', 'green', 'blue', 'white', 'gold']
colors.extend(["black","violet"]) # ['pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors) 


colors.insert(0,"steelblue") # ['steelblue', 'pink', 'green', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)


#remove value and index
colors.remove("green") # ['steelblue', 'pink', 'blue', 'white', 'gold', 'black', 'violet']
print(colors)


#remove from end value and index
colors.pop() # ['steelblue', 'pink', 'blue', 'white', 'gold', 'black']
print(colors)



#remove value and index
del colors[1] # ['steelblue', 'blue', 'white', 'gold', 'black']
del colors[1:3] # ['steelblue', 'gold', 'black']
print(colors)



vals = [1,2,3,4,5]
print(f"Before clear values {vals}") # Before clear values [1, 2, 3, 4, 5]
vals.clear()
print(f"After clear values {vals}") # After clear values []


boys = ["aung aung","zaw zaw","kyaw kyaw","hein min","yae lay","min khant"]
boys.sort()
print(boys) # ['aung aung', 'hein min', 'kyaw kyaw', 'min khant', 'yae lay', 'zaw zaw']

boys.reverse()
print(boys) # ['zaw zaw', 'yae lay', 'min khant', 'kyaw kyaw', 'hein min', 'aung aung']


nums = [10,115,11,1,50,30,75,25,65,90,110]
nums.sort()
print(nums) # [1, 10, 11, 25, 30, 50, 65, 75, 90, 110, 115]

nums.reverse()
print(nums) # [115, 110, 90, 75, 65, 50, 30, 25, 11, 10, 1]


ages = [18,25,30,18,30,25,25,20,18,25]
countof18 = ages.count(18)
print(countof18) # 3

countof20 = ages.count(20)
print(countof20) # 1 

countof25 = ages.count(25)
print(countof25) # 4


print(ages.index(20)) #7
print(ages.index(30)) #2


# nested list 
numbers = [[1,2,3],[40,50,60],[700,800,900]]
print(len(numbers)) # 3
print(numbers[0]) # [1, 2, 3]
print(numbers[1]) # [40, 50, 60]
print(numbers[2]) # [700, 800, 900]
# print(numbers[3]) # error
print(numbers[2][0]) # 700
print(numbers[2][2]) # 900


numbers.append([1000,2000])
print(numbers) # [[1, 2, 3], [40, 50, 60], [700, 800, 900], [1000, 2000]]

numbers.pop()
print(numbers) # [[1, 2, 3], [40, 50, 60], [700, 800, 900]]

numbers.pop(1)
print(numbers) # [[1, 2, 3], [700, 800, 900]]



greeting = ["Hello","Su Su"]
print(" ".join(greeting)) # Hello Su Su
print("-".join(greeting)) # Hello-Su Su


print(greeting[0]) # Hello
print(greeting[1]) # Su Su

val1,val2 = greeting
print(val1) # Hello
print(val2) # Su Su