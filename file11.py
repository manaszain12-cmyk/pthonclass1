                 #While Loop Exercise:
s1 = 'python prOgramming'

l = len(s1)
x = 0
while x < l:
    if s1[x].lower() not in 'aeiou':#!= 'a' and s1[x] != 'e' and s1[x] != 'i' and s1[x] != 'o' and s1[x] != 'u':
        print(s1[x])
    x = x + 1

print('Exit')

x = 1
sum = 0
while x <= 100:
    sum = sum + x
    x = x + 1

print(sum)

sum = 0
x = ''
while x != 'N':
    x = input('Pleas enter any number to add or enter N to exit')
    if x != 'N':
        sum = sum + int(x)

print(sum)





