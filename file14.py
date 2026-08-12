                 #Python Continue and Break

#Continue
i = 1
while i <= 5:
    if i == 3:
        i = i + 1
        continue
    print(i)
    i = i + 1
 
s1 = ('Hello python')
for x in s1:
    if x in 'aeiou ':
        continue
    print(x)

#Break
s1 = ('Hello python')
for x in s1:
    if x in ' ':
        break
    print(x)
print('Done')

sum = 0
while True:
    x = input('Pleas enter any number to add or enter N to exit')
    if x == 'N':
        break
    sum = sum + int(x)

print(sum)

s1 = ('Hello python')
for x in s1:
    if x in ' ':
        break
    print(x)
else:
    print('FFAAAAAAAHHHHHHHHHHHHHHHH')
