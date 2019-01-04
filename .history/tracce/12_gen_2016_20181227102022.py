""" 
input
tol tolleranza
maxIter numero massimo iterate

output
approssimazione di s^1/3
numIter numero di iterate effetuate
"""

def radCubic(s,tol,maxIter):
    if s < 1:
        print('value inserted not correct')
        return False
    x0 = s
    niter = 0
    valoreFisso = 1/3
    while x0 > s and niter < maxIter:       
        x1 = valoreFisso*(2*x0+(s/(x0**2)))
        x0 = x1
        niter += 1
    return(x0,niter)

print(radCubic(1234,10**-9,100))
