a, b = 1, 2
resultat = 0

while b <= 4000000:
    if b % 2 == 0:
        resultat += b
    a, b = b, a + b

print(resultat)
