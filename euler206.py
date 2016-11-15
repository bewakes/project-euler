import re
test = '1[0-9]2[0-9]3[0-9]4[0-9]5[0-9]6[0-9]7[0-9]8[0-9]9[0-9]'

for n in range(1000000,9999999):
    n1 = int('3'+str(n)+'30')
    n2 = int('3'+str(n)+'70')
    n3 = int('4'+str(n)+'30')
    n4 = int('4'+str(n)+'70')
    n5 = int('1'+str(n)+'30')
    n6 = int('1'+str(n)+'70')


    if re.match(test, str(n1**2)):
        print(n1, n1**2)
        break
    if re.match(test, str(n2**2)):
        print(n2, n2**2)
        break
    if re.match(test, str(n3**2)):
        print(n3, n3**2)
        break
    if re.match(test, str(n4**2)):
        print(n4, n4**2)
        break
    if re.match(test, str(n5**2)):
        print(n5, n5**2)
        break
    if re.match(test, str(n6**2)):
        print(n6, n6**2)
        break
