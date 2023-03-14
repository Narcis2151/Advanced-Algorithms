def determinant(x1, y1, x2, y2, x3, y3):
    return 1*(x1*y2 + x2*y3 + x3*y1) - x1*y3 - x2*y1 - x3*y2

t = int(input())
lista_rezultate = [0, 0, 0]
lista_puncte = [] 

for i in range(t):
    x1, y1 = map(int, input().split())
    lista_puncte.append((x1, y1))

for i in range(t-1):
    if i == t-2:
        rez = determinant(lista_puncte[i][0], lista_puncte[i][1], lista_puncte[i+1][0], lista_puncte[i+1][1], lista_puncte[0][0], lista_puncte[0][1])
    else:
        rez = determinant(lista_puncte[i][0], lista_puncte[i][1], lista_puncte[i+1][0], lista_puncte[i+1][1], lista_puncte[i+2][0], lista_puncte[i+2][1])
        
    if rez > 0:
        lista_rezultate[0] += 1
    elif rez < 0:
        lista_rezultate[1] += 1
    else:
        lista_rezultate[2] += 1
    
print(*lista_rezultate)