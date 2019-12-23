# String formatting

name = 'Johny'
age = 32
title = 'Sony'
price = 100

print('My name is ' + name + ' and I\'m ' + str(age) + ' old.')
print('My name is %(name)s and I\'m %(age)d old.' % {'name': name, 'age': age})
print('My name is %s and I\'m %d old. %s' % (name, age, name))
print('Title: %s, price: %.2f' % ('Sony', 100))

# Modern method .format
print('Title: {1}, price: {0}'.format(title, price))
print('Title: {title}, price: {price}'.format(title=title, price=price))

# F-strings
print(f'Title: {title}, price: {price}. This is the most popular method.')
