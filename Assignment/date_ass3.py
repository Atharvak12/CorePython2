
from datetime import *

ints = date.today()

print("Current date :-", ints)
# print("Current date ", ints.day)
# print("Current Month ",ints.month)
# print("Current Year ",ints.year)

c = 0
for i in ints :
    c = c + i
    print(c)


next_month = ints + timedelta(days = 30)
print("after 30 day :-", next_month)
