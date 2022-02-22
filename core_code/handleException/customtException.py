try:
    age=int(input("Enter Your Age\n"))
    if age>=18:
        print("You are eligible to cast vote")
    else:
        raise Exception("Invalid Voter")
except Exception as m:
    print(m)