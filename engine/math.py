from pygame.math import Vector2, Vector3
from pygame.rect import Rect
from math import pi

def RadToDeg(rad):
    return rad * 180 / pi

def DegToRad(deg):
    return deg / 180 * pi

def  WorldToScreenPos(pos):
    return Vector2(pos)*10

def BezierCurve(count, p0, p1, p2, p3):
    pairs = []

    v0 = p0
    for i in range(1, count+1):
        j = i / count
        ij = (1-j)
        v1 = (ij**3)*Vector2(p0) + 3*(ij**2)*j*Vector2(p1) + 3*ij*(j**2)*Vector2(p2) + (j**3)*Vector2(p3)
        pairs.append([v0, v1])
        v0 = v1
    
    return pairs

class RectF:
    def __init__(self, left, top, width, height):
        self._left = left
        self._top  = top
        self._width = width
        self._height = height

    @property
    def left(self):
        return self._left

    @property
    def top(self):
        return self._top

    @property
    def right(self):
        return self._left + self._width

    @property
    def bottom(self):
        return self._top + self._height

    @property
    def centerx(self):
        return self._left + self._width / 2
    
    @property
    def centery(self):
        return self._top + self._height / 2

    @property
    def center(self):
        return (self.centerx, self.centery)

    @property
    def lefttop(self):
        return (self.left, self.top)

    @property
    def righttop(self):
        return (self.right, self.top)

    @property
    def leftbottom(self):
        return (self.left, self.bottom)

    @property
    def rightbottom(self):
        return (self.right, self.bottom)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def position(self):
        return (self._left, self._top)

    @property
    def size(self):
        return (self._width, self._height)

    def move(self, pos):
        ret = RectF(self._left + pos[0], self._top + pos[1], self._width, self._height)

        return ret

    def collidePoint(self, pos):
        xaxis = self.left <= pos[0] and pos[0] <= self.right
        yaxis = self.top  <= pos[1] and pos[1] <= self.bottom

        return xaxis and yaxis

    def collide(self, rect):
        xaxis = self.left <= rect.right  and rect.left <= self.right
        yaxis = self.top  <= rect.bottom and rect.top  <= self.bottom

        return xaxis and yaxis

    def __str__(self):
        return 'RectF ({}, {}, {}, {})'.format(self._left, self._top, self._width, self._height)