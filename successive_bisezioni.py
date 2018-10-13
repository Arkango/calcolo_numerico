# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 
import matplotlib.pyplot as plt

def bisezioni(f,a,b,tol,nmax):
    x=.5*(a+b)
    fa=f(a)
    fx=f(x)
    niter=0
    res =[]
    res.append(fx)
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    while niter < nmax and .5*(b-a) > tol:  
        if fa*fx<0:
            b=x
        else:
            a=x
            fa=fx
        x=.5*(a+b)
        fx=f(x)
        res.append(fx)
        niter += 1
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    if .5*(b-a) > tol:
        niter = -1 
    return (x,niter,res)

def newton(f,df,x0,tol,nmax):
    a=3.141592653589793
    niter =0
    err=tol+1
    
    print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    while err>tol and niter<nmax:
        dfx0 = df(x0)
        if dfx0 == 0:
            niter = -1
            return(x0,niter)
        fx0=f(x0)
        dx =-fx0/dfx0
        x1=x0+dx
        err=abs(dx)
        niter+=1
        x0=x1
        print('{:2}\t {:1.16f}\t {:+1.1e} \t {:+1.1e}'.format(niter,x0,abs(a-x0),err))
    return (x0,niter)

def regulafalsi(f,a,b,tol,nmax):
    x= b-(f(a)*(b-a)/(f(b)-f(a)))
    fx= f(x)
    fa=f(a)
    niter = 0
    res =[]
    res.append(fx)
    
    print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    
    while niter < nmax and b-(f(a)*(b-a)/(f(b)-f(a))) > tol:
        if fx*fa<0:
            b=x
        else:
            a=x
            #fa=fx
        niter+=1
        x= b-(f(a)*(b-a)/(f(b)-f(a)))
        fx= f(x)
        res.append(fx)
        print('{:2}\t {:1.16f}\t {:+1.1e}'.format(niter,x,fx))
    return (x,niter,res)

def corde():
    

def f(x) : return x**3-(4*x)
def df(x): return np.cos(x)

x0=3.10
tol=1
nmax = 100
out=regulafalsi(f,0.5,6,tol,nmax)
""""
x=np.arange(0,out[1]+1)
y=np.array(out[2])
y=np.abs(y)        
plt.semilogy(y)"""