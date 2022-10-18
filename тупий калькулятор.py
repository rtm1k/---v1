#тупий калькулятор

from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.GREEN)

what = input('Що робити? (+, -):')

a = float( input ('Введіть перше число: ') )
b = float( input ('Введіть друге число: ') )

if what == '+':
    c = a + b
    print ('Результат: ' + str(c))
elif what == '-':
    c = a - b
    print('Результат: ' + str(c))
else:
    print('Вибрано неправильну дію')

input()