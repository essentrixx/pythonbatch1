lady = {"name":"Yandanar","age":30}

print(lady) # {'name': 'Yandanar', 'age': 30}
print(lady.get('name')) # Yandanar
print(lady.get('gender')) # None
print(lady.get('gender','Not Defined')) # Not Defined

print(lady.keys()) # dict_keys(['name', 'age'])
print(list(lady.keys())) # ['name', 'age']
print(list(lady.keys())[0]) # name
print(list(lady.keys())[1]) # age
 

print(lady.values()) # dict_values(['Yandanar', 30])
print(list(lady.values())) # ['Yandanar', 30]
print(list(lady.values())[0]) # Yandanar
print(list(lady.values())[1]) # 30


print(lady.items()) # dict_items([('name', 'Yandanar'), ('age', 30)])
print(list(lady.items())) # [('name', 'Yandanar'), ('age', 30)]
print(list(lady.items())[0]) # ('name', 'Yandanar')
print(list(lady.items())[1]) # ('age', 30)
print(list(lady.items())[0][0]) # name
print(list(lady.items())[0][1]) # Yandanar
print(list(lady.items())[1][0]) # age
print(list(lady.items())[1][1]) # 30



lady.update({'age':20,'gender':'female'})
print(lady) # {'name': 'Yandanar', 'age': 20, 'gender': 'female'}

lady.pop('age')
print(lady) # {'name': 'Yandanar', 'gender': 'female'}

lady.clear()
print(lady) # {}

# boy = {'name':'Zaw Zaw','city':'Yangon'}
# boy.pop()
# print(boy) # erroe

girl = {'name':'Yandanar','age':30,'city':'Mawlamyine'}

item = girl.popitem()
print(item) # ('city', 'Mawlamyine')
print(item[0]) # city
print(item[1]) # Mawlamyine

print(girl) # {'name': 'Yandanar', 'age': 30}


woman = girl.copy() 
print(woman) # {'name': 'Yandanar', 'age': 30}

