s = r'Some string \and \test'  # raw string
print(s)

name = 'John'
age = 20
print('My name is ' + name + '. I\'m ' + str(age))
print(len(name))

if len(name):
    print('Name has length')

print(name[0:len(name)])

