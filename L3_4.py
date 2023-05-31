def intersectie(inecuatii, punct):
    xmax = 10000000001
    ymax = 10000000001
    xmin = -10000000001
    ymin = -10000000001

    for inecuatie in inecuatii:
        
        if inecuatie[0] * punct[0] + inecuatie[1] * punct[1] + inecuatie[2] >= 0:
            continue

        if inecuatie[0] == 0:
            if inecuatie[1] < 0:
                ymin = max(ymin, (-1) * inecuatie[2] / inecuatie[1])
            else:
                ymax = min(ymax, (-1) * inecuatie[2] / inecuatie[1])

        else:
            if inecuatie[0] < 0:
                xmin = max(xmin, (-1) * inecuatie[2] / inecuatie[0])
            else:
                xmax = min(xmax, (-1) * inecuatie[2] / inecuatie[0])
    
    if xmax != 10000000001 and ymax != 10000000001 and xmin != -10000000001 and ymin != -10000000001:
        aria = (xmax - xmin) * (ymax - ymin)
        return("YES\n" + "{:.6f}".format(aria))
    
    return("NO")

inecuatii = []
puncte = []
n =  int(input())
for i in range(n):
    coeficienti = [int(x) for x in input().split()]
    inecuatii.append(coeficienti)
    
m = int(input())
for i in range(m):
    coeficienti = [float(x) for x in input().split()]
    puncte.append(coeficienti)

for punct in puncte:
    output = intersectie(inecuatii, punct)
    print(output)