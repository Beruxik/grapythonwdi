import random
x = random.randint(0, 100)
print(x)
usernum = 0

while usernum != x:
    try:
        usernum = int(input('Podaj liczbę od 1 do 100: '))
        if usernum > x:
            print('za duża liczba')
            usernum = int(input('Podaj liczbę od 1 do 100: '))
        if usernum < x:
            print('za mała liczba')
            usernum = int(input('Podaj liczbę od 1 do 100: '))
        if usernum == x:
            print('brawo, mój przyjacielu')
    except ValueError:
        print('Nie podałeś liczby!')
