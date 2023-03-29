def is_x_monotone(points):

    if len(points) < 3:
        return True
    
    min_index = points.index(min(points, key=lambda p: p[0]))
    max_index = points.index(max(points, key=lambda p: p[0]))
    if min_index < max_index:
        monotone = True
        for i in range(min_index, max_index):
            if points[i][0] > points[i+1][0]:
                monotone = False
                break

    else:
        monotone = True
        for i in range(max_index, min_index):
            if points[i][0] < points[i+1][0]:
                monotone = False
                break
    
    return monotone


def is_y_monotone(points):
    if len(points) < 3:
        return True
    
    min_index = points.index(min(points, key=lambda p: (p[1], p[0])))
    max_index = points.index(max(points, key=lambda p: (p[1], p[0])))
    if min_index < max_index:
        
        monotone = True
        #print(min_index, max_index)
        for i in range(min_index, max_index):
            #print(points[i])
            if points[i][1] > points[i+1][1]:
                monotone = False
                break
    else:
        monotone = True
        for i in range(max_index, min_index):
            #print(points[i])
            if points[i][1] < points[i+1][1]:
                monotone = False
                break   

    return monotone

n = int(input())
varfuri = []
for i in range(n):
    x1, y1 = map(int, input().split())
    varfuri.append((x1, y1))
    
x_monotone = is_x_monotone(varfuri)
y_monotone = is_y_monotone(varfuri)
if x_monotone:
    print("YES")
else:
    print("NO")
if y_monotone:
    print("YES")
else:
    print("NO")