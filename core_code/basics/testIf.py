# price=500
# budget =int(input("Enter Your Budget\n"))
# if(budget>=price):
#     print("You can enjoy your Pizza")

#if-else
# price=500
# budget =int(input("Enter Your Budget\n"))
# if(budget>=price):
#     print("You can enjoy your Pizza")
# else:
#     print("You can not buy pizza. pizza price starts from ",price)
#     print("You need {} more".format(price-budget))


#at the time of multiple choices 
#elif ladder
# budget =int(input("What is Your Budget?\n"))
# if budget>=400:
#     print("You can buy a large size chizz Pizza")
# elif budget>=300:
#     print("You can buy a Medium size chizz Pizza")
# elif budget>=200:
#     print("You can buy a small size chizz Pizza")
# elif budget>=99:
#     print("You can buy a regular  Pizza")
# else:
#     print("You can buy burgers above 40 Rs.")


#Nested If else 
pre,mains,merit=88,79,80
if(pre>=merit):
    if mains>=merit:
        print("You are selected")
    else:
        print("Your mains score {m} is below the merit list criteria {c}".format(c=merit,m=mains))
else:
    print("Your pre score {} is below the merit list criteria {}".format(pre,merit))