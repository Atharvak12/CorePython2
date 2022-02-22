import os
print(os.getcwd())
# os.mkdir("D:/Atharv")
# print("folder created")

# #multiple
# os.makedirs("Atharv/python/basic/io")
# print("folderes created")

# os.rename("D:/Atharv","D:/Rays")

# os.removedirs("d:/Rays")

#how to list
dirs=os.listdir("D:/")
i=1
for x in dirs:
    print(i," ",x)
    i+=1