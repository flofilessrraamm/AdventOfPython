

clavier = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9))

current = (1,1) #on commence à 5 (index 1,1 dans la matrice du clavier)
code = ''

def move(cmd, current):
    if cmd == 'U':
        if current[0] > 0:
            current = (current[0] - 1, current[1])
    elif cmd == 'D':
        if current[0] < 2:
            current = (current[0] + 1, current[1])
    elif cmd == 'L':
        if current[1] > 0:
            current = (current[0], current[1] - 1)
    elif cmd == 'R':
        if current[1] < 2:
            current = (current[0], current[1] + 1)
    return current


f = open('input.txt')

for line in f:
    for char in line:
        current = move(char, current)
    code += str(clavier[current[0]][current[1]])
print('le code est ', code)

