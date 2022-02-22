#empty set
s=set()

print(type(s))

s1={1,1,1,11,2,3,4}
s2={1,2,3}
print(type(s1))
print(s1)# tuple will omit the duplicate'

#set is unordered
# print(s1[0])
# print(s1[0:2])
print(max(s1))
print(min(s1))
print(sum(s1))
print(s1.issuperset(s2))
print((s1.issubset(s2)))
print((s2.issubset(s1)))
print((s1.intersection(s2)))
for e in s1:
    print(e)

