#strings
str1='string with single quote'
str2="string with double quote"
str3='''

this is multiline string

'''
print(str1)
print(str2)
print(str3)

#extract chars using indexing
my_str="My string is name"
print(my_str[0])
#extracting each element
for x in my_str:
    print(x)

#string length using len() function
print("length of my_string : ", len(my_str))

#check if substring(including space) is present or not in string
print("is n" in my_str)
print("is ne" in my_str)

if "is n" in my_str:
    print("'is n' is present in my_string: ",my_str)

print("is n" not in my_str)
print("is ne" not in my_str)

if "is ne" not in my_str:
    print("yes it is not in my_string", my_str)
