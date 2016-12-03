def testTriangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

f = open('input.txt')
possibles = []
compteur = 0
triangles = []
for line in f:
    compteur+=1
    sides = line.split()
    triangles.append((sides[0], sides[1], sides[2]))
    if compteur == 3:
        compteur = 0
        for i in range(3):
            if testTriangle(int(triangles[0][i]), int(triangles[1][i]), int(triangles[2][i])):
                possibles.append((triangles[0][i], triangles[1][i], triangles[2][i]))
        triangles = []

print("nb de vrai triangles: ", len(possibles))
for triangle in possibles:
    print("\n" + triangle[0] + " " + triangle[1] + " " + triangle[2])
