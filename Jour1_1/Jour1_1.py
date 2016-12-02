import math

f = open('input.txt', 'r')
commandes = f.read().split(', ')

pos = (0, 0)
dir = 0

mem = set()
mem.add(pos)
firstIntersection = None

moveSet = (
    {'L' : 3, 'R' : 1},  #nord
    {'L' : 0, 'R' : 2},  #est
    {'L' : 1, 'R' : 3},  #sud
    {'L' : 2, 'R' : 0},  #ouest
    )


for cmd in commandes:
    dist = int(cmd[1:])
    dir = moveSet[dir][cmd[0]]
    sign = -1 if dir -2 >= 0 else 1
    axis = dir%2    #0 is x, 1 is y

    
    for i in range(dist):
        pos = (pos[0], pos[1] + sign) if axis == 1 else (pos[0] + sign, pos[1])
        if firstIntersection == None:
            if pos in mem:
                firstIntersection = pos
            mem.add(pos)
                 
    
print("the headquarter is at ", abs(pos[0]) + abs(pos[1]), "blocks and\nthe nearest place your path crossed is at ", abs(firstIntersection[0]) + abs(firstIntersection[1]), " blocks")

