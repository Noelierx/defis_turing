import random
import time

#Algorithme de tri par sélection

def trisel(T):
    n=len(T)
    for i in range(0,n-1):
        k=i
        for j in range(i+1,n):
              if T[j]<=T[k]:
                 k=j
                 (T[i],T[k])=(T[k],T[i])
        return(T)
    
        

bornesup = 100000
liste = []
for i in range(10000):
    liste.append(random.randint(0, bornesup))
td=time.time()
print(td)
liste=trisel(liste)

tf=time.time()
duree=tf-td
print(liste)
print('Durée :',duree,' s')
