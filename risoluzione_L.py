import numpy as np

def risolviL(L,b):
    result = []

    result.append( b.item(0)/L.item(0, 0))
    for i in range(1,3):
        val = 0
        for x in range(0,i):
            val += result[x]*L.item(i,x)
        result.append((b.item(i) + ((-1)*val))/L.item(i,i))
    return result


L = np.matrix([[1,0,0],[-0.5,1,0],[-0.5,0,1]])
b = np.array([[4,9,2]])

print(risolviL(L,b))