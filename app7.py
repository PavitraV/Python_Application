# Defines two classes, Point() and Disk().
# The latter has an "area" attribute and three methods:
# - change_radius(r)
# - intersects(disk), that returns True or False depending on whether
#   the disk provided as argument intersects the disk object.
# - absorb(disk), that returns a new disk object that represents the smallest
#   disk that contains both the disk provided as argument and the disk object.


from math import pi, hypot, sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x:.2f}, {self.y:.2f})'


class Disk:
    area = 0

    def __init__(self, *, centre=Point(0,0), radius=0):
        self.radius = radius
        self.centre = centre
        self.area = pi * radius * radius

    def __repr__(self):
        return f'Disk({Point(self.centre.x,self.centre.y)}, {self.radius:.2f})'

    def change_radius(self, r):
        self.radius = r
        self.area = pi * r * r

    def intersects(self, disk):
        flag = False
        if (disk.centre.x == self.centre.x or disk.centre.y == self.centre.y):
            if(self.centre.x>disk.centre.x):
                x1 = self.centre.x
                x2 = disk.centre.x
            else:
                x2 = self.centre.x
                x1 = disk.centre.x
            if (abs(disk.radius - self.radius) > 0 or x2+disk.radius == x1-self.radius ):
                flag = True
        return flag

    def absorb(self, disk):
        dist = sqrt((self.centre.x - disk.centre.x) ** 2 + (self.centre.y - disk.centre.y) ** 2)
        maxrad = max(self.radius,disk.radius)
        minrad = min(self.radius, disk.radius)
        if(maxrad == self.radius):
            newx = self.centre.x
            newy = self.centre.y
        else:
            newx = disk.centre.x
            newy = disk.centre.y
        if(dist+minrad<=maxrad):
            return Disk(centre = Point(newx,newy), radius = maxrad)
        newrad = (self.radius + disk.radius + dist) / 2
        d = dist + disk.radius - newrad
        newx = self.centre.x + (d * (disk.centre.x - self.centre.x) / sqrt(
            (disk.centre.x - self.centre.x) ** 2 + (disk.centre.y - self.centre.y) ** 2))
        newy = self.centre.y + (d * (disk.centre.y - self.centre.y) / sqrt(
            (disk.centre.x - self.centre.x) ** 2 + (disk.centre.y - self.centre.y) ** 2))
        d = Disk(centre = Point(newx, newy), radius = newrad)
        return d

disk_1 = Disk(centre = Point(7, -2), radius = 8)
disk_2 = Disk(centre = Point(4.5, 1), radius = 4)
print(disk_1.intersects(disk_2))
