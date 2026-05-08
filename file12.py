# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(j, end = ' ')
        j = j + 1
    print()
    i = i + 1

print('After while')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end = ' ')
        j = j + 1
    print()
    i = i + 1

print('After while')

# *
# * *
# * * *
# * * * *
# * * * * *

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end = ' ')
        j = j + 1
    print()
    i = i + 1

print('After while')

i = 1
while i <= 5:
    print('*'* i, sep = ' ')
    i = i + 1

print('After while')
