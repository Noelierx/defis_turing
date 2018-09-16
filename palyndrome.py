def miroir (nb):
    nb=str(nb)
    nb=nb[::-1]
    nb=int(nb)
    return nb

nb=10000000
while miroir(nb) !=4*nb:
    nb+=-1


print(nb)


