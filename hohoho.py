"""Hohoho."""
from time import sleep
from os import system
import platform

E = '\033[0m'
R = '\033[0;31m'
G = '\033[0;32m'
Y = '\033[1;33m'

a = 1
print('')
for j in range(100):
    if platform.system().lower() == 'windows':
        system('cls')
    else:
        system('clear')
    print('  ')
    print(Y + ' ' * 11 + '    *' + E)
    print(Y + ' ' * 11 + '   ***' + E)
    print(Y + ' ' * 11 + ' *******' + E)
    print(Y + ' ' * 11 + '  ** **' + E)
    print(Y + ' ' * 11 + '  *   *' + E)
    for i in range(15):
        if ((i + j) % 2 == 0):
            print(R + ' ' * (15 - (a // 2)) + '*' * a + ' ' * (15 - (a // 2)) + E)
            a += 2
        else:
            print(G + ' ' * (15 - (a // 2)) + '*' * a + ' ' * (15 - (a // 2)) + E)
            a += 2
    if(j % 2 == 0):
        print(G + ' ' * (a // 2) + '*' + E)
        print(R + ' ' * (a // 2) + '*' + E)
        print(G + ' ' * (a // 2) + '*' + E)
    else:
        print(R + ' ' * (a // 2) + '*' + E)
        print(G + ' ' * (a // 2) + '*' + E)
        print(R + ' ' * (a // 2) + '*' + E)
    a = 1
    sleep(0.5)
