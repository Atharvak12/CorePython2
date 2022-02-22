f=open("Data.txt","a")
sl="this is a line"
ml=["First Line\n","second Line\n","Third Line\n"]
f.write(sl)#writes single line to file
f.writelines(ml)#write multiple lines at once
f.close()
print("data saved")
