import numpy as np

def risolviL(L,b):
    result = []

    for i in range(0,3):
        l_current = 0
        for x in range(0,3):
            if x != i:
                if i == 0 :
                    value = 0
                else:
                    value = result[i-1]
                l_current += L.item((i,x))*-1*value
        result.append(b.item(i)*L.item((i,i)) + l_current)
    return result


L = np.matrix([[1,0,0],[-0.5,1,0],[-0.5,0,1]])
b = np.array([[4,9,2]])

print(risolviL(L,b))