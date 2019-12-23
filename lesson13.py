counter = 1

# while counter <= 10:
#     print(counter)
#     counter += 1

# checkingString = 'Sabbra-cadabra'
#
# for letter in checkingString:
#     if letter == '-':
#         continue
#     print(letter, sep=' ')
# else:
#     print('After loop')

currentYear = int(input('Enter your year '))
baseYear = 1900

while baseYear <= currentYear:
    print(f'Year: {baseYear}')
    baseYear += 1

