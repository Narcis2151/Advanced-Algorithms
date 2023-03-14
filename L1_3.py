def determinant(x1, y1, x2, y2, x3, y3):
    return 1*(x1*y2 + x2*y3 + x3*y1) - x1*y3 - x2*y1 - x3*y2

def get_start_point(lista_puncte):
    min_point = min(lista_puncte, key=lambda x: (x[1], x[0]))
    return lista_puncte.index(min_point)

def acoperire_convexa(lista_puncte, min_point):
    current = min_point
    acoperire = [lista_puncte[current]]
    while True:
        succesor = (current + 1) % len(lista_puncte)
        for i in range(len(lista_puncte)):
            if determinant(lista_puncte[current][0], lista_puncte[current][1], lista_puncte[i][0], lista_puncte[i][1], lista_puncte[succesor][0], lista_puncte[succesor][1]) < 0:
                succesor = i
        if succesor == min_point:
            break
        else:
            current = succesor
            acoperire.append(lista_puncte[succesor])
    return acoperire[::-1]
    
t = int(input())
lista_puncte = [] 

for i in range(t):
    x1, y1 = map(int, input().split())
    lista_puncte.append((x1, y1))
#print(get_start_point(lista_puncte))
acoperire = acoperire_convexa(lista_puncte, get_start_point(lista_puncte))
print(len(acoperire))
for i in acoperire:
    print(*i)
    
    

