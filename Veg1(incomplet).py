from isn import *
from math import cos, sin
coefl=0.3
coefa=0.7
pi=3.141592653

def fougere (x1,y1,x2,y2,n): 
  if n==0 :
      drawLine(x1,y1,x2,y2,0,255,0)
  else :
    xa,ya=similit(x1,y1,x2,y2,0.85,pi-0.05)
    xb,yb = similit(x1,y1,x2,y2,coefl,pi*coefa)
    xc,yc = similit(x1,y1,x2,y2,coefl,-pi*coefa)
    drawLine(x2, y2, xa, ya,0,255-20*n,0)
    drawLine(x2, y2, xb, yb,0,255-20*n,0)
    drawLine(x2, y2, xc, yc,0,255-20*n,0)

# il reste a effectuer trois appels recursifs de la fonction sur chacun des segments précédemment tracés 
    fougere(x2, y2, xa, ya,n-1)                     
    fougere(x2, y2, xb, yb,n-1)                     
    fougere(x2, y2, xc, yc,n-1) 

def similit (x1,y1,x0,y0,coeff,angle):
    xu=coeff*(cos(angle)*(x1-x0)-sin(angle)*(y1-y0))+x0
    yu=coeff*(sin(angle)*(x1-x0)+cos(angle)*(y1-y0))+y0
    return xu,yu

initDrawing("DessinRécursif",10,10,400,600)
drawLine(200,570,200,470,0,55,0)          
fougere (200,570,200,470,10)
showDrawing()
