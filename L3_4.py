def intersectie(inecuatii, punct):
    xmaxim = 10000000001
    ymaxim = 10000000001
    xminim = -10000000001
    yminim = -10000000001

    for inecuatie in inecuatii:
        
        if inecuatie[0] * punct[0] + inecuatie[1] * punct[1] + inecuatie[2] >= 0:
            continue

        if inecuatie[0] == 0:
            if (-1) * inecuatie[2] / inecuatie[1] < punct[1]:
                yminim = max(yminim, (-1) * inecuatie[2] / inecuatie[1])
            else:
                ymaxim = min(ymaxim, (-1) * inecuatie[2] / inecuatie[1])

        else:
            if (-1) * inecuatie[2] / inecuatie[0] < punct[0]:
                xminim = max(xminim, (-1) * inecuatie[2] / inecuatie[0])
            else:
                xmaxim = min(xmaxim, (-1) * inecuatie[2] / inecuatie[0])
    
    if xmaxim != 10000000001 and ymaxim != 10000000001 and xminim != -10000000001 and yminim != -10000000001:
        return("YES\n" + "{:.6f}".format((xmaxim - xminim) * (ymaxim - yminim)))
    
    return("NO")

inecuatii = []

n =  int(input())


for i in range(n):
    line = [int(x) for x in input().split()]

    inecuatii.append(line)

puncte = []

m = int(input())

for i in range(m):
    line = [float(x) for x in input().split()]

    puncte.append(line)

for punct in puncte:

    output = intersectie(inecuatii, punct)
    print(output)