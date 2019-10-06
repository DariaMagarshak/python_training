from geom2d import *

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
#l2 = list(map(lambda p: Point(p.x, -p.y), l))

l2 = list(filter(lambda p: p.x % 2 == 0, l))





#l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]

#def x(p):
    #return p.x


#def y(p):
    #return p.y


#l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

#print(l1)
#print(l2)

# list comprehention
#l = [Point (i, i*i) for i in range (-5, 6)]
#l2 = [Point(el.x, - el.y) for el in l]

#for i in range (-5, 6):
    #l.append(Point(i, i*i))

#l2 = []

#for el in l:
    #l2.append(Point(el.x, - el.y))

print(l)
print(l2)


