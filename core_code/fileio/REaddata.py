# f=open("data.txt")#default is reading mode
# #OR
# # f=open("data.txt", "r")
# data=f.read()#read whole data at once
# print(data)
# f.close()


# f=open("data.txt")#default is reading mode
#OR
# f=open("data.txt", "r")
# print(f.read(5))#read 5 characters
# f.close()


# f=open("data.txt", "r")
# print(f.readline())# read a single line
# f.close()


# f=open("data.txt", "r")
# print(f.readlines())# read multiple line and returns a list
# f.close()

#line by line reading
f=open("data.txt")
for line in f:
    print(line,end="")
