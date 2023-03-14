def determinant(x1, y1, x2, y2, x3, y3):
    return 1*(x1*y2 + x2*y3 + x3*y1) - x1*y3 - x2*y1 - x3*y2

t = int(input())
lista_rezultate = []

for i in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    if determinant(x1, y1, x2, y2, x3, y3) == 0:
        lista_rezultate.append("TOUCH")
    elif determinant(x1, y1, x2, y2, x3, y3) > 0:
        lista_rezultate.append("LEFT")
    else:
        lista_rezultate.append("RIGHT")

print(*lista_rezultate, sep='\n')
    

