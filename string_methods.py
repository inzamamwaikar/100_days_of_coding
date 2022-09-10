str="Subhash Vayugundala"
print(str.capitalize())
print(str.upper())
print(str.casefold())
print(str.lower())
print(str.center(41,"*")) #**********Subhash Vayugundala***********
print(str.endswith("Vayugundala"))
print(str.endswith("la"))

#find
str1="Subhash Vayugundala is 21 years old"
print(str1.find("a"))
print(str1.find("25"))
if str1.find("21")>0:
    print("FOUND")
else:
    print("not FOUND")

if str1.find("26")>0:
    print("FOUND")
else:
    print("not FOUND")

if "21" in str1:
    print("FOUND 21")
else:
    print("not FOUND 21")

print(str1.find("a", 10, 18))


print(str1.index("a"))
str2="Sangli123"
print(str1.isalnum()) #false bcoz space is not aplphanumeric
print(str2.isalnum())
str2="Sangli"
print(str1.isalpha())
print(str2.isalpha())

str2="1233453453"
print(str1.isdigit())
print(str2.isdigit())
str2="1233453453"
str3="1233.53"
print(str2.isdigit())
print(str2.isnumeric())
print(str3.isdigit())
print(str3.isnumeric())
print(str3.isdecimal())


str4="Hello! Are you #1?"
print(str4)


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)


#transalte is similar to replace but not in inplace
txt = "Hello Sam!"
print(id(txt))
mytable = txt.maketrans("S", "P")
txt1=txt.translate(mytable)
print(txt1)
print(id(txt1))

txt = "Hello Sam!"
print(id(txt))
print(txt.replace("S","P"))
print(id(txt))
print(txt)



txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
print(type(x))

print(list(x))
print(type(x))



txt = '''welcome
      to the jungle
      '''
x = txt.split()
print(x)
x = txt.split("to")
print(x)

print(txt.startswith("wel"))
