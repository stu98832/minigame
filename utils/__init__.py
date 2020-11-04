import pygame
from math import pi

def RadToDeg(rad):
    return rad * 180 / pi

def DegToRad(deg):
    return deg / 180 * pi

def BezierCurve(count, p0, p1, p2, p3):
    pairs = []

    v0 = p0
    for i in range(1, count+1):
        j = i / count
        v1 = ((1-j)**3)*pygame.Vector2(p0) + 3*((1-j)**2)*j*pygame.Vector2(p1) + 3*(1-j)*(j**2)*pygame.Vector2(p2) + (j**3)*pygame.Vector2(p3)
        pairs.append([v0, v1])
        v0 = v1
    
    return pairs