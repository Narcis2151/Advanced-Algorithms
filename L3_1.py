def det(triunghi, punct):
    xa, ya, xb, yb, xc, yc = triunghi[0][0], triunghi[0][1], triunghi[1][0], triunghi[1][1], triunghi[2][0], triunghi[2][1]
    xd, yd = punct[0], punct[1]
    mat = [[xa, ya, xa**2 + ya**2, 1], [xb, yb, xb**2 + yb**2, 1], [xc, yc, xc**2 + yc**2, 1], [xd, yd, xd**2 + yd**2, 1]]
    det = 0
    def det3x3(mat):
        return (mat[0][0] * mat[1][1] * mat[2][2]
                + mat[0][1] * mat[1][2] * mat[2][0]
                + mat[0][2] * mat[1][0] * mat[2][1]
                - mat[0][2] * mat[1][1] * mat[2][0]
                - mat[0][0] * mat[1][2] * mat[2][1]
                - mat[0][1] * mat[1][0] * mat[2][2])
    
    for i in range(4):
        submat = [mat[j][:i] + mat[j][i+1:] for j in range(1, 4)]
        sgn = (-1) ** i  
        cof = mat[0][i] * det3x3(submat)
        det += sgn * cof
        
        
    if det > 0:
        return "INSIDE"
    elif det == 0:
        return "BOUNDARY"
    else:
        return "OUTSIDE"
    
    
triunghi = []
for i in range(3):
    x, y = input().split()
    x, y = int(x), int(y)
    triunghi.append((x, y))
    
puncte = []
m = int(input())
for i in range(m):
    x, y = input().split()
    x, y = int(x), int(y)
    puncte.append((x, y))
    
for i in range(m):
    print(det(triunghi, puncte[i]))