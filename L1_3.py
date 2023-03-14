def determinant(x1, y1, x2, y2, x3, y3):
    return 1*(x1*y2 + x2*y3 + x3*y1) - x1*y3 - x2*y1 - x3*y2

def get_start_point(lista_puncte):
    start_point = min(lista_puncte, key=lambda x: (x[1], x[0]))
    return lista_puncte.index(start_point)
    
def acoperire_convexa(lista_puncte, index_min):

    l_inf = [lista_puncte[index_min], lista_puncte[index_min + 1]]
    index_min += 2
    
    for i in range(2, len(lista_puncte)):
        
        if index_min == len(lista_puncte):
            index_min = 0
            
        l_inf.append(lista_puncte[index_min]) 
        print(l_inf)
        
        while len(l_inf) > 2 and determinant(l_inf[-3][0], l_inf[-3][1], l_inf[-2][0], l_inf[-2][1], l_inf[-1][0], l_inf[-1][1]) <= 0:
            l_inf.pop(-2)
            
        index_min += 1
    return l_inf


    
t = int(input())
lista_puncte = [] 

for i in range(t):
    x1, y1 = map(int, input().split())
    lista_puncte.append((x1, y1))
#print(get_start_point(lista_puncte))
acoperire = acoperire_convexa(lista_puncte, index_min = get_start_point(lista_puncte))
print(len(acoperire))
for i in acoperire:
    print(*i)