#open a file in reading mode
f=None
try:
    f=open("Test.txt")
    #read method reads all data from the file at once
    # print(f.read())
    
    # print(f.read(5))#5 char at once
    # print(f.readline())#read a single line
    # for line in f.readlines():
    #     #return a list of line
    #     print(line,end="")
    
    for line in f:
        #return a list of line
        print(line,end="")
    
except FileNotFoundError:
    print("File Does not exist")
finally:
    try:
        f.close()
    except Exception:
        print("Could not close")