resultat = 0

for i in range(1, 2013):
    if i%5 == 0 or i%7 == 0:
        resultat += i

print(resultat)
