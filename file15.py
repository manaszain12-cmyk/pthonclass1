#                      #List

# fruit_names = ['Apple', 'Mango', 'Grapes', 'Melon', 'Guava']
# print(fruit_names)

# print(type(fruit_names))

# print(fruit_names[3])

# print(fruit_names[-3])

# print(fruit_names[1:5])

# print(len(fruit_names))

# #cccc
#                 #or
# marks = list( (40, 50, 60, 70, 80, 90, 100) )
# print(marks)

# print('Grapes' in fruit_names)

# print('Grapes' not in fruit_names)

fruit_names = ['Apple', 'Mango', 'Grapes', 'Melon', 'Guava']
# fruit_names[1] = 'Banana'

# fruit_names.append('Peach')

# fruit_names.insert(3, 'Orange')

# fruit_names.remove('Grapes')

# fruit_names.pop()

# del fruit_names[2]
# print(fruit_names)

# test_list = ['table', 100, 60.7, True, fruit_names]
# print(test_list)

marks = [120, 200, 150, 220, 180]

# for m in marks:
#     print(m)

l = len(marks)
i = 0

while i < l:
    print(marks[i])
    i += 1

#Find the max number in any list
marks = [120, 200, 150, 220, 180]
max = marks[0]
for m in marks:
    if m < max:
        max = m

print(max)

#List Comprehension

even = []
numbers = [20, 50, 68, 89, 100, 119, 34, 8, 19]
for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)

# newlist = [ expression for item in iterable if condition == True]






