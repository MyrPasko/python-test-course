list1 = [2, 3, 'a', 'hello', ['1', 'a'], True]
print(list1)

list2 = list('Hello')
print(list2, sep='\n')

list3 = list((1, 2, 3))
print(list3)

list4 = [i for i in 'hello world motherfuckers' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
print(list4)

name = 'tom'
array = ['mike', 'tom']
print('jon' not in array)

list5 = list(range(5, 10, 2))
print('--List5--', list5)

for i in range(5):
    print(f'An external loop #{i}')
    for j in range(5):
        if j != 0:
            print(f'\tAn internal loop #{j}')

base = list(range(1, 11))

for i in base:
    for j in base:
        print(f'{i} * {j} = {i * j}')
    print(' ')
