def determinant(x1, y1, x2, y2, x3, y3):
    return x2*y3 + x3*y1 + x1*y2 - x2*y1 - x3*y2 - x1*y3 

def get_smallest_point(points):
    smallest_point = min(points, key=lambda x: (x[0], x[1]))
    smallest_index = points.index(smallest_point)
    return smallest_index, smallest_point

def result(varfuri, punct):
    
    min_x, max_x, min_y, max_y = varfuri[0][0], varfuri[0][0], varfuri[0][1], varfuri[0][1]
    for i in range(1, len(varfuri)):
        min_x = min(min_x, varfuri[i][0])
        max_x = max(max_x, varfuri[i][0])
        min_y = min(min_y, varfuri[i][1])
        max_y = max(max_y, varfuri[i][1])
    if punct[0] < min_x or punct[0] > max_x or punct[1] < min_y or punct[1] > max_y:
        return "OUTSIDE"
    
    minim = 0
    maxim = len(varfuri) - 1
    while (maxim - minim > 1):
        mid = (minim + maxim) // 2
        if determinant(varfuri[minim][0], varfuri[minim][1], punct[0], punct[1], varfuri[mid][0], varfuri[mid][1]) >= 0:
            maxim = mid
        else:
            minim = mid 
            
    if determinant(varfuri[minim][0], varfuri[minim][1], punct[0], punct[1], varfuri[maxim][0], varfuri[maxim][1]) == 0:
        return "BOUNDARY"
    if determinant(varfuri[minim][0], varfuri[minim][1], punct[0], punct[1], varfuri[maxim][0], varfuri[maxim][1]) < 0:
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
    
smallest_index, smallest_point = get_smallest_point(varfuri)
varfuri_sortate = []
varfuri_sortate += varfuri[smallest_index:] 
varfuri_sortate += varfuri[:smallest_index]
for i in range(m):
    print(result(varfuri, puncte[i]))