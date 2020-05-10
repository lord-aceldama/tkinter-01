from tkinter import *
import math
import random

D = 600         #-- Size of the tkinter window
o = int(D / 2)  #-- The center point

def cross(P : int) -> list:
    """ Returns points for the wibbly cross with a specified 
        distance (P) between points.
    """
    global D, o
    
    #-- Get the maximum number of points
    n = int((D -1) / (2 * P))

    L = list()
    for x in range(-n, n+1):
        y = n - abs(x)
        L.append([o+(P*x), o, o, o+(P*y)])
        L.append([o+(P*x), o, o, o-(P*y)])

    L = L[1:-1] #-- Removes the double lines where x = n and -n
    return L


def mess(P : int) -> list:
    """ Draws P messy lines
    """
    global D

    L = list()
    for i in range(P):
        L.append([random.randint(0, D) for x in range(4)])
    return L


def polygon(P : int) -> list:
    """ Draws a polygon with given number of points (P)
    """
    global D
    L = list()
    op = [random.randint(0, D) for x in range(2)]
    for i in range(P):
        np = [random.randint(0, D) for x in range(2)]
        L.append(op + np)
        op = np

    #-- Connect last point to first
    L.append(op + L[0][0:2])

    return L


def circle(P : int) -> list:
    """ Draws a circle with given number of points (P)
    """
    def pget(r: int, i : int, d : float) -> list:
        """ Calculates the x-y coordiates of a point on a circle given 
            the radius of the circle, the point's index (i) and degree 
            between two points (d).
        """
        global o

        radians_to_degrees = math.pi / 180
        x = r * math.cos(i * d * radians_to_degrees)
        y = r * math.sin(i * d * radians_to_degrees)
        return  [o + x, o + y]

    global D

    L = list()
    r = int(D / 2) - 5
    d = 360 / float(P)
    op = pget(r, 0, d)
    for i in range(1, P):
        np = pget(r, i, d)
        L.append(op + np)
        op = np

    #-- Close the circle
    L.append(op + L[0][0:2])

    return L


def trippy_circle(P : int) -> list:
    """ Like circle, but connects all nodes
    """
    C = circle(P)
    L = list()
    for i in range(len(C)):
        for j in range(len(C)):
            if i != j:
                L.append(C[i][0:2] + C[j][0:2])

    return L


def draw(c : Canvas, L : list, color : str):
    """ Instead of drawing lines connected to each other, draw loose, single lines
    """
    for ln in L:
        c.create_line(ln, fill=color)


root = Tk()
root.geometry("{0}x{0}".format(D))
c = Canvas(root, width=D, height=D, bg="black")
c.grid(row=0, column=0)

draw(c, mess(30), "magenta")
draw(c, trippy_circle(20), "navy")
draw(c, polygon(10), "yellow")
draw(c, cross(10), "red")
draw(c, circle(50), "light green")

root.mainloop()