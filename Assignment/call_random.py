
import random
print("Give the range :")
x=int(input("start point"))
y=int(input("end point"))

# randomlist = []
# for i in range(0,5):                            # 5 no choos e kerne ke liye
#     n = random.randint(1,100)                   # range define kerne ke liye 1 - 100
#     randomlist.append(n)
# print(randomlist)


# randomlist = random.sample(range(x,y), 5)
# print(randomlist)

randomlist = [ random.randrange(x,y,1) for i in range(5)]
print(randomlist)
