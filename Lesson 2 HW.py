Solutions:
2.1. health = int(input('Введите уровень здоровья вашего персонажа: '))
     if health > 0:
         print('True')
     else:
    	 print('False')

2.2. number = int(input('Введите любое число: '))
     if number%2:
         print('Нечетное')
     else:
         print('Четное')

number = int(input('Введите любое число: '))
if number % 2:
print('Четное')
else:
print('Нечетное')


2.3.

# С вложенными условиями
year = int(input())
if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print('Високосный')
        else:
            print('Невисокосный')
    else:
        print('Високосный')
else:
    print('Невисокосный')

# C логическими операторами

if not year%4 and year%100 or not year%400:
    print('Високосный')
else:
    print('Невисокосный')

2.4.
# С циклом while/while loop

text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
i = 1
while i <= num:
    print(text)
    i += 1

# С циклом for/for loop

num = int(input('Enter the number of repetitions: '))
for i in range(1, num+1):
    print(i, text)