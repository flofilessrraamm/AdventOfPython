def testTriangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False

f = open('input.txt')
possibles = []

for line in f:
    sides = line.split()
    if testTriangle(int(sides[0]), int(sides[1]), int(sides[2])):
        possibles.append((sides[0], sides[1], sides[2]))

print("nb de vrai triangles: ", len(possibles))
for triangle in possibles:
    print("\n" + triangle[0] + " " + triangle[1] + " " + triangle[2])
