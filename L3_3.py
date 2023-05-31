def intersectie(inecuatii):
    xmax = 10000000001
    ymax = 10000000001
    xmin = -10000000001
    ymin = -10000000001

    for inecuatie in inecuatii:

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

    if ymin > ymax or xmin > xmax:
        return "VOID"
    elif xmin != -10000000001 and ymin != -10000000001 and xmax != 10000000001 and ymax != 10000000001:
        return "BOUNDED"
    else:
        return "UNBOUNDED"

inecuatii = []

n =  int(input())
for i in range(n):
    coeficienti = [int(x) for x in input().split()]
    inecuatii.append(coeficienti)

print(intersectie(inecuatii))
