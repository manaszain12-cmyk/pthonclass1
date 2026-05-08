                 #Strig
x = 'Pakistan'
print(x)
print( type(x) )

#Multiline
y = '''Test 1
Line 1
Line 2
Line3
'''
print(y)
print( type(y) )

#Arrays
x = 'Python Program'
print(x[2])
print(x[-6])

#Lenght
#If we want to know length, we use "len"
print( len(x) )

#String "in" and "not in"
print( 'thon' in (x) )
print( 'thor' not in (x) )

#Slicing strings
z = 'I love Pakistan'
print(z[0:10])
print(z[2:])
print(z[:10])
print(z[-8:10])

#String Concatenation
s1 = 'Great'
s2 = 'Pakistan'
s3 =  s1 +' '+ s2 
print(s3)

print('Great'+' Pakistan')

print(s2*5)

#String format
qty = 2
item = 'Apple'
price = 30.50
s1 = 'I want {2} kg {1} for {0} dollars'
print(s1.format(qty, item , price))

#Escape Sequencing
t1 = "Pakistan is a \n \"great\" country"
print(t1)

#Methods
a = 'I love Pakistan'
print(a.upper())

b = 'i am strong'
print(b.islower())