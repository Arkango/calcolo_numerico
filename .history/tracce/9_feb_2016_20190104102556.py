def metodo0(f,h,tol,x0,maxIter):
    numIter = 0
    x1 = x0 - ((2 * h)*(f(x0)/(f(x0+h)-f(x0-h))
    while((x0-x1)/x0 > tol and numIter < maxIter):
        x1= x1 - ((2 * h)*(f(x1)/(f(x1+h)-f(x1-h))
        numIter +=1
    return(x1,numIter)
