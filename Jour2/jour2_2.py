
def move(cmd, current):
    if cmd == 'U':
        if checkMoveLegality(current, (current[0]-1, current[1])):
                current = (current[0] - 1, current[1])
    elif cmd == 'D':
        if checkMoveLegality(current, (current[0]+1, current[1])):
            current = (current[0] + 1, current[1])
    elif cmd == 'L':
        if checkMoveLegality(current, (current[0], current[1]-1)):
            current = (current[0], current[1] - 1)
    elif cmd == 'R':
        if checkMoveLegality(current, (current[0], current[1]+1)):
            current = (current[0], current[1] + 1)
    return current

def checkMoveLegality(pos1, pos2):
    rules = {0:(2,),
            1:(1,2,3),
            2:(0,1,2,3,4),   #allowed next indexes from every index (colums or rows have the same rules)
            3:(1,2,3),
            4:(2,)}
    if pos2[0] in rules[pos1[1]] and pos2[1] in rules[pos1[0]]:
        return True
    else:
        return False


clavier = ((0, 0, 1, 0, 0), 
           (0, 2, 3, 4, 0),  #if a zero pops up in the code, there is a problem!
           (5, 6, 7, 8, 9), 
           (0, 'A', 'B', 'C', 0), 
           (0, 0, 'D', 0, 0))

current = (2,0) #on commence à 5 (index 2,0 dans la matrice du clavier)
code = ''

f = open('input.txt')

for line in f:
    for char in line:
        current = move(char, current)
    code += str(clavier[current[0]][current[1]])
print('le code est ', code)

