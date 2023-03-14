def determinant(x1, y1, x2, y2, x3, y3):
    return x2*y3 + x3*y1 + x1*y2 - x2*y1 - x3*y2 - x1*y3     

n = int(input())
points = [] 

for i in range(n):
    x1, y1 = map(int, input().split())
    points.append((x1, y1))
acoperire = [points[0], points[1]]

for i in range(2, n):
        acoperire.append(points[i])
        while len(acoperire)>2 and determinant(acoperire[-3][0], acoperire[-3][1], acoperire[-2][0], acoperire[-2][1], acoperire[-1][0], acoperire[-1][1])<=0: 
            del acoperire[-2]
while len(acoperire)>2 and determinant(acoperire[-2][0], acoperire[-2][1], acoperire[-1][0], acoperire[-1][1], acoperire[0][0], acoperire[0][1])<=0:
    del acoperire[-1]
while len(acoperire)>2 and determinant(acoperire[-1][0], acoperire[-1][1], acoperire[0][0], acoperire[0][1], acoperire[1][0], acoperire[1][1])<=0:
    del acoperire[0]
while len(acoperire)>2 and determinant(acoperire[0][0], acoperire[0][1], acoperire[1][0], acoperire[1][1], acoperire[2][0], acoperire[2][1])<=0:
    del acoperire[1]
    
print(len(acoperire))
for i in acoperire:
    print(*i)



