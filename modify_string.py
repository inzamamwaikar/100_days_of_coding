str1 = '  Subhash Vayugundala  '
#Modifying string
print(str1.upper())
print(str1.lower())
print(str1.strip())
print(str1.replace('a', 'x'))
print(str1.replace('s', 'x'))
print(str1.split('a'))
print(len(str1.split('a')))

#concatination string
a="subhash"
b="vayugundala"
print(a+b)
a="1"
b=2
print(a+str(b))

#fomatting string
age=21
name="ABC"
print(name + format(age))
print(name ,age)

#escape chars for " '
print("We are the so-called \"Vikings\" from the north.")
print("We are the so-called \'Vikings\' from the north.")
print("We are the so-called \n Vikings\n from the north.")
print("We are the so-called \t Vikings \t from the north.")
print("We are the so-called    \b Vikings    \b from the north.")

