#open a binary file for reading
src=open("C:\\Users\\DELL\\OneDrive\Pictures\\Indore.jpg",'rb')
dest=open("CopyImage.jpg","wb")
dest.write(src.read())
src.close()
dest.close()
print("Successfully copied")