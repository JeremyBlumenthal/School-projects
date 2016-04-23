#INFO-F-101 school project: Vasarely-like drawer with turtle graphics

from turtle import goto,setpos,color,up,down,begin_fill,end_fill
from math import sin,radians
EPS = 1.0e-5 #Deformation constant
col1,col2,col3 = input('Color 1: '),input('Color 2: '),input('Color 3: ')
longueur = int(input("Hexagon side length: " ))
centre_cercle = int(input('Centre of circle (x coordinate): ')),int(input('Centre of circle (y): ')),int(input('Centre of circle (z): '))
rayon = int(input('Radius: '))
inf_gauche = int(input('Lower left corner coordinate (eg. -300): '))
sup_droit = int(input('Upper right corner (eg. 300): '))

def deformation(p,c,r):
    """
    Returns p after deformation
    """
    def distance(p,q):
       """distance entre les 2 points p et q"""
       return ((q[0]-p[0])**2 + (q[1]-p[1])**2 + (q[2]-p[2])**2)**0.5
    d = distance(p,c) 
    if d >= r:
        res = p
    else:
        if d > EPS: 
            facteur = r/d
        else:
            facteur = 1
        x2 = c[0] + (p[0]-c[0]) * facteur
        y2 = c[1] + (p[1]-c[1]) * facteur
        z2 = c[2] + (p[2]-c[2]) * facteur
        res = (x2,y2,z2)
    return res
deform = lambda p: deformation(p,centre_cercle,rayon)

def hexagone(c, longueur,m, col1, col2, col3,deform):
    """
    Draws a hexagon with or without deformation
    """
    lo = longueur
    x,y,z = c #Hexagon centre
    pa1,pa2,pa3 = (x+lo,y,z), (x+(lo/2),y-m,z), (x-(lo/2),y-m,z)#First losange coordinates (lower right)
    pb1,pb2,pb3 = (x+lo,y,z), (x+(lo/2),y+m,z), (x-(lo/2),y+m,z)#Losange 2 (upper right)
    pc1,pc2,pc3 = (x-(lo/2),y+m,z), (x-lo,y,z), (x-(lo/2),y-m,z)#Losange 3 (left)
    pts = [pa1,pa2,pa3,c,pb1,pb2,pb3,c,pc1,pc2,pc3,c]
    d = []
    for point in pts:
        xd,yd,zd = deform(point)
        d.extend((xd,yd))
    up()
    setpos(d[6],d[7])#Turtle resets to c
    down()
    col = [col1,col2,col3]
    i = 0
    for e in col:
        color(e)
        begin_fill()
        goto(d[i],d[i+1])
        goto(d[i+2],d[i+3])
        goto(d[i+4],d[i+5])
        goto(d[i+6],d[i+7])
        end_fill()
        i += 8
        
def pavage(inf_gauche,sup_droit,longueur,col1,col2,col3,deform):
    """
    Paves hexagons with function hexagone
    """
    x,y,z = inf_gauche,inf_gauche,0
    x_initial = x
    m = longueur*sin(radians(60))
    ligne = 0 
    while y <= sup_droit:
        while x <= sup_droit:
            hexa = hexagone((x,y,z),longueur,m,col1,col2,col3,deform)
            x += 3*longueur
        if ligne % 2 != 0:
            x = x_initial
        else:
            x = x_initial + ((3/2)* longueur)
        y += m
        ligne += 1
       
tableau = pavage(inf_gauche,sup_droit,longueur,col1,col2,col3,deform)