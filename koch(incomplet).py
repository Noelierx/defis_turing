from isn import *
from math import cos, sin

pi=3.141592653

def koch(x1,y1,x2,y2,n):
   if n == 0 : 
      drawLine(x1, y1, x2, y2,255,0,0)
   else:
      xa,ya=similit(x2,y2,x1,y1,1/3,0)
      xb,yb=similit(x2,y2,x1,y1,2/3,0)
      xc,yc = similit(xa,ya,xb,yb,1,pi/3);
#appel récursif sur les quatre segments
      koch(n-1)
      

def similit (x1,y1,x0,y0,coeff,angle):
    xu=coeff*(cos(angle)*(x1-x0)-sin(angle)*(y1-y0))+x0
    yu=coeff*(sin(angle)*(x1-x0)+cos(angle)*(y1-y0))+y0
    return xu,yu

initDrawing("DessinRécursif",10,10,1000,500)
koch(30,400,930,400,10)
showDrawing()
