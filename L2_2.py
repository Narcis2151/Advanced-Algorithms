def determinant(x1, y1, x2, y2, x3, y3):
    return x2*y3 + x3*y1 + x1*y2 - x2*y1 - x3*y2 - x1*y3 

def result(varfuri, punct):
    nr = 0

    for i in range(len(varfuri)):
        p1 = varfuri[i]
        p2 = varfuri[(i + 1) % len(varfuri)]
        if(p1[1] == p2[1] and p1[1] == punct[1] and min(p1[0], p2[0]) <= punct[0] and max(p1[0], p2[0]) >= punct[0]):
            return "BOUNDARY"
        if(p1[0] == p2[0] and p1[0] == punct[0] and min(p1[1], p2[1]) <= punct[1] and max(p1[1], p2[1]) >= punct[1]):
            return "BOUNDARY"
        if (p1[1] > punct[1]) != (p2[1] > punct[1]):
            if punct[0] < (p2[0] - p1[0]) * (punct[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
                nr += 1
            elif punct[0] == (p2[0] - p1[0]) * (punct[1] - p1[1]) / (p2[1] - p1[1]) + p1[0]:
                return "BOUNDARY"
    if nr % 2 == 1:
        return "INSIDE"
    return "OUTSIDE"

n = int(input())
varfuri = []
for i in range(n):
    x1, y1 = map(int, input().split())
    varfuri.append((x1, y1))
    
m = int(input())
puncte = []
for i in range(m):
    x1, y1 = map(int, input().split())
    puncte.append((x1, y1))

for i in range(m):
    print(result(varfuri, puncte[i]))
    