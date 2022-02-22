#create a file in CWD
#files open in reading mode by default
#open funtion opens the text file in reading mode by default
# f=open("TEst.txt",'w')
f=open("Test.txt","a")
#if file exit it will open for writing
#if not exist than 1st create it and than open for writing
# f.write("Hello","Worlds")#generate error
for i in range(10):
    f.write("Hello world\n")
f.writelines(["Rays\n","Atharv\n","Ashsih\n"])#write mutiple lines
print("data saved successfully")