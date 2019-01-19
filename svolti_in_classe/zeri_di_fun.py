import numpy as np
import matplotlib.pyplot as plt


def bisezioni(f, a, b, tol, nmax):
    x = .5 * (a + b)
    fa = f(a)
    fx = f(x)
    niter = 0
    res = []
    res.append(fx)
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter, x, fx))
    while .5 * (b - a) > tol and niter < nmax:
        if fa * fx < 0:
            b = x
        else:
            a = x
            fa = fx
        x = .5 * (a + b)
        fx = f(x)
        res.append(fx)
        niter += 1
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter, x, fx))
    if .5 * (b - a) > tol:
        niter = -1
    return (x, niter, res)


def newton(f, df, x0, tol, nmax):
    niter = 0
    err = tol + 1
    res = []
    res.append(f(x0))
    print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter, x0, err))
    while err > tol and niter < nmax:
        dfx0 = df(x0)
        if dfx0 == 0:
            niter - 1
            return (x0, niter)
        fx0 = f(x0)
        dx = -fx0 / dfx0
        x1 = x0 + dx
        err = abs(dx)
        niter += 1
        res.append(f(x1))
        print('{:2}\t {:1.15f}\t {:+1.1e}'.format(niter, x0, err))
        x0 = x1
    return (x1, niter, res)


def f(x): return x - np.cos(x)


def df(x): return 1 + np.sin(x)


x0 = 0.7
tol = 1e-15
nmax = 100

print('\n\t succ bisezioni\n')
out_bis = bisezioni(f, 0, 1, tol, nmax)
print('\n\t newton\n')
out_newt = newton(f, df, x0, tol, nmax)

x_bis = np.arange(0, out_bis[1] + 1)
y_bis = np.array(out_bis[2])
y_bis = np.abs(y_bis)
plt.semilogy(x_bis, y_bis)

x_newt = np.arange(0, out_newt[1] + 1)
y_newt = np.array(out_newt[2])
y_newt = np.abs(y_newt)
plt.semilogy(x_newt, y_newt)
