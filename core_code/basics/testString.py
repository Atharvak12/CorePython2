#python string
#single line string
s1='rays'
s2="Rays"
#multiline string
s3='''aaaaarays tech'''
s4="""Rays
Technology"""
print(type(s1))
print(type(s2))
print(type(s3))
print(type(s4))
print("Uppercase:",s3.upper())
print("Lowercase:",s3.lower())
print("Capital case:",s3.capitalize())
print("Title:",s3.title())
print("Starts With:",s3.startswith("a"))
print("ends With:",s3.endswith("ch"))
print("strip:",s3.strip())
print("Count:",s3.count("a"))
print("Starts With:",s3.find("te"))
print("Starts With:",s3.replace("rays","SunilOs"))
