# Programme ISN

from isn import *
#Tête
initDrawing("Cercle",50,50,400,400)
drawCircle(100,50,30,0,0,0)
"""Tracé d'un cercle"""
global canvas
couleur = "#%02x%02x%02x" % (0,0,0)
#Corps
initDrawing("rectangle",50,50,400,400)
rawRect(x1,y1,x2,y2,rouge,vert,bleu)
"""Tracé d'un rectangle"""
global canvas
couleur = "#%02x%02x%02x" % (rouge,vert,bleu)

showDrawing()
