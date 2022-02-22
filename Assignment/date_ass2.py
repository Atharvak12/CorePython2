from datetime import *


# # today_date = date.today()
# def diff(start, end):
#     return (end - start).days

start = str(input('Enter date(yyyy-mm-dd): '))
my_date = datetime.strptime(start, "%Y-%m-%d")

end = str(input("Enter end date (yyyy-mm-dd):"))
my_date2 = datetime.strptime(end, "%Y-%m-%d")

diff = my_date2- my_date
# print(diff(my_date2,my_date), "days")

if my_date2 > my_date:
    print(diff)
else:
    print("Error")
