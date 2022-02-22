import os#this module deals with the os related functions
print("Get CWD:",os.getcwd())
#create folder
# os.mkdir("TestPython")#it will create a directory/folder into a CWD
# os.mkdir("D:/TestPython")#it will create a directory/folder into a D: Drive

#create multiple directories
# os.makedirs("TestPython/core/io")
# print("Directory Created:")

# os.rmdir("TestPython")
# print("Folder deleted:")

#list all the files and folders in the directory
l=os.listdir("D:/")
count=0
for i in l:
    count=count+1
    print(count ,"\t",i)
# print(l)