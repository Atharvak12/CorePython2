import random
# l=[2,1,3,4,6,8,'a']
# print(random.choice(l))


# print(random.randrange(1,10,2))
# print(random.uniform(1,10))

#default limit 0,1
# print(random.random())
#wheneever you want same random number then use seed
# random.seed()#default value is system time
# print(random.randint(1,1000))

# print(random.randrange(10,20))
# ra=random.random()#0 to 1
# ra=random.random()*100#0 to 100
import math
min=4
max=10
ra=math.floor(random.random()*(max-min+1)+min)#4 to 10
print(ra)#0 to 1

#wAP to generate 4 digit OTP number
#WAp to generate 6 character capetcha
