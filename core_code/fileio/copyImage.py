source="C:\\Users\\DELL\\OneDrive\\Pictures\\indore.jpg"
#open a image file in reading mode
src=open(source,"rb")
# open a image file in writing mode1
des=open("CopyOfIndore.jpg","wb")
for line in src:
    des.write(line)

src.close()
des.close()
print("Image copied successfully")

