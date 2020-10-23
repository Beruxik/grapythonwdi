import random
x = random.randint(1, 100)
print(x)
usernum = 0
gorna = 100
dolna = 1

while usernum != x:
    try:
        usernum = int(input('Podaj liczbę od ' + str(dolna) + ' do ' + str(gorna) + ': '))
        if x < usernum <= gorna:
            print('za duża liczba')
            gorna = usernum - 1
        elif x > usernum >= dolna:
            print('za mała liczba')
            dolna = usernum + 1
        elif usernum > gorna or usernum < dolna:
            print('Podaj liczbę z podanego zakresu!')
        else:
            print('brawo, mój przyjacielu')
    except ValueError:
        print('Nie podałeś liczby!')
