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
    while x0 > s and niter < maxIter:
        


