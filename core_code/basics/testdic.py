#dictonary stores data in key=value pair
#it is unordered
#it is mutable

#empty dictonary
d={}
print(type(d))
d1=dict()
print(type(d1))

data={
    1:"Atharv",
    "age":20,
    "salary":40.5,
    5.9:"height"
}
print(data)
#add one more pair
data["address"]="Indore"
print(data)
data["Address"]="pune"
print(data)

#get data 
print(data["Address"])
print(data.get('Address'))

#all keys
keys=data.keys()
print(keys)
for key in keys:
    value=data.get(key)
    print("{}={}".format(key, value))
    
#get all values
values=data.values()
print(values)

for v in values:
    print(v)

#get key value pair
items=data.items()
print(items)
for i in items:
    print(i)

#if you want to remove
print("POP",data.pop(1))
del data["Address"]
print("after delete:",data)
    
#all the methods
# print(help(data))

#add more data
ad={"course":"Python","age":19}
data.update(ad)
print(data)

