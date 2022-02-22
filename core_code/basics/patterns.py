print("--------pattern 1-------------------")
for row in range(1,6):
    for col in range(1,6):
        print(col,end=' ')
    print("")
    
print("--------pattern 2-------------------")
for row in range(1,6):
    for col in range(1,6):
        print(row,end=' ')
    print("")
    
print("--------pattern 3-------------------")
for row in range(1,6):
    for col in range(1,row+1):
        print(row,end=' ')
    print("")

print("--------pattern 4-------------------")
for row in range(1,6):
    for col in range(5,row-1,-1):
        print(col,end=' ')
    print("")

print("--------pattern 5-------------------")
for row in range(1,6):
    for col in range(5,row-1,-1):
        print(row,end=' ')
    print("")

print("--------pattern 6-------------------")
for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end='')
    for col in range(1,row+1,1):
        print(col,end='')
    print("")

print("--------pattern 7-------------------")
for row in range(1,6):
    for space in range(1,row,1):
        print(" ",end='')
    for col in range(5,row-1,-1,):
        print(col,end='')
    print("")

print("--------pattern 8-------------------")
for row in range(1,6):
    for space in range(1,row,1):
        print(" ",end='')
    for col in range(5,row-1,-1,):
        print(col,end=' ')
        
    print("")

print("--------pattern 9-------------------")
for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end='')
    for col in range(1,row+1,1):
        print(row,end=' ')
    print("")
    
print("--------pattern 9-------------------")
for row in range(1,6):
    for space in range(5,row,-1):
        print(" ",end='')
    for col in range(1,row+1,1):
        if row==3 and col==2:
            print("N", end=" ")
        else:   
            print(row,end=' ')
    print("")
