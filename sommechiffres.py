def sommechiffres(nb):
    s=str(nb)
    som=0
    for i in s:
        som+=int(i)
    return(som)

print(sommechiffres(2^2222**1000))
