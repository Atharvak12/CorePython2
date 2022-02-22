age=int(input("Enter your age\n"))#global vraiable
try:
    if(age>=18):
        print("You can cast vote")
    else:
        #custom exception message
        raise Exception("You are under 18")
except Exception as e:
    print("Error:",e)
    
