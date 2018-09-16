# Ces programmes sont sous licence CeCILL-B V1.

from isn import *

fichier = openIn("joconde.ppm")
s = readLineFromFile(fichier)
s = readLineFromFile(fichier)
largeur = int(readStringFromFile(fichier))
hauteur = int(readStringFromFile(fichier))
maximum = int(readStringFromFile(fichier))

rouge = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]
vert  = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]
bleu  = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]

for j in range(0,hauteur):
  for i in range(0,largeur):
    rouge[i][j] = int(readStringFromFile(fichier))
    vert [i][j] = int(readStringFromFile(fichier))
    bleu [i][j] = int(readStringFromFile(fichier))
close(fichier)

rougebis = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]
vertbis = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]
bleubis = [[255 for j in range(0,hauteur)] for i in range(0,largeur)]

#Modification de l'image
for i in range(largeur):
  for j in range(hauteur):
    rougebis[i][j] =rouge[i][j]
    vertbis[i][j] =vert[i][j]
    bleubis[i][j] =bleu[i][j]
    


# Écriture du fichier ppm
fichier2 = openOut("joconde2.ppm")
print("P3",file=fichier2)
print("#",file=fichier2)
print(largeur,file=fichier2)
print(hauteur,file=fichier2)
print(maximum,file=fichier2)
for j in range(0,hauteur):
  for i in range(0,largeur):
    print(rougebis[i][j],file=fichier2)
    print(vertbis[i][j],file=fichier2)
    print(bleubis[i][j],file=fichier2)
    
close(fichier2)

initDrawing("Avant                                Après",10,10,2*largeur,hauteur)
for j in range(hauteur):
  for i in range(largeur):
    drawPixel(i,j,rouge[i][j],vert[i][j],bleu[i][j])
for j in range(hauteur):
  for i in range(largeur):
    drawPixel(largeur+i,j,rougebis[i][j],vertbis[i][j],bleubis[i][j])

showDrawing()


