def det(patrulater):
    xa, ya, xb, yb, xc, yc, xd, yd = patrulater[0][0], patrulater[0][1], patrulater[1][0], patrulater[1][1], patrulater[2][0], patrulater[2][1], patrulater[3][0], patrulater[3][1]
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
        return "ILLEGAL"
    else:
        return "LEGAL"
    
patrulater = []
for i in range(4):
    patrulater.append(tuple(map(int, input().split())))

print("AC: " + det(patrulater))
patrulater = patrulater[1:] + [patrulater[0]]
print("BD: " + det(patrulater))