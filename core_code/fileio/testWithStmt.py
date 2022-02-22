# with open("Data.txt") as f:
#     print(f.read())


f=open("Data.txt")
lines=f.readline()
while(lines!=None):
    print(lines)
    lines=f.readline()

f.close()