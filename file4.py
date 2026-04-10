x = 100
y = 200
z = 300
#print(x, y, z)

#print('Hello1', 'Hello2', ';Hello43')
#print('Hello1', 'Hello2', 'Hello3', sep = '---')

print('hello python 1', end = '^')
print('hello python 2', end = '^')
print('hello python 3')

name = 'Anas'
country = 'Pakistan'
age = '13'
#print('My name is',name,'and i live in',country)
#print('My name is '+name+' and i live in '+country)
#print('My name is '+name+' and i am '+str(age) )
print(f'My name is {name} and i am {age}' )

# input starts here
name = input('Please enter your name: ')
print(f'Your name is {name}')

x = int(input('Piease enter x:'))
y = int(input('Piease enter y:'))
z = x + y
print(f'Sum of {x} and {y} is {z}')