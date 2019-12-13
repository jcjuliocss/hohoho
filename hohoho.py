from time import sleep
from os import system

E = '\033[0m'
R = '\033[0;31m'
G = '\033[0;32m'

a = 1
print ''
for j in range(100):
    system('clear')
    for i in range(10):
        if ((i+j)%2==0):
            print R + ' '*(10-(a//2))+'*'*a+' '*(10-(a//2)) + E
            a += 2
        else:
            print G + ' '*(10-(a//2))+'*'*a+' '*(10-(a//2)) + E
            a += 2
    if(j%2==0):
        print R + ' '*(a//2) + '*' + E
        print G + ' '*(a//2) + '*' + E
    else:
        print G + ' '*(a//2) + '*' + E
        print R + ' '*(a//2) + '*' + E
    a = 1
    sleep(0.5)
