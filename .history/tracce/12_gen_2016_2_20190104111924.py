def secanti(f,x0,x1,tol,maxIter):
    numIter = 0
    x2 = x1 - ((f(x1)*(x1-x0))/(f(x1)-f(x2)))
    while (x0-x2)/x0 < tol and numIter < maxIter:
        x2 = 