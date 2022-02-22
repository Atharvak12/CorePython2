# f=open("Test.txt",'w')#create a file in CWD


#if files exist ,then opens a file in a writing  mode else 
#first it will create the file into the specified path and
#open it for the writing 
# f=open("D:/Test.txt",'w')
f=open("D:/Test.txt",'a')#append mode
print("File created")
for i in range(1,6):
    f.writelines("Rays {}\n".format(i))

# f.close()
print("data saved successfully")

