# Thanks to https://malishoaib.wordpress.com/2014/05/30/inverse-of-incomplete-beta-function-computational-statisticians-wet-dream/

import math
 
################################################################
 
def invincompbeta(p, a, b):
     
    ''' invincompbeta(p,a,b) evaluates inverse of incomplete beta function, here 1 <= p <= 0 and a, b > 0. This function requires incompbeta(a,b,x) and contfractbeta(a,b,x, ITMAX = 200)
    (C ++ Code translated into Python from: Numerical Recipes in C; 3rd ed.)'''
     
    a1=a-1.0
    b1=b-1.0
    ERROR = 1.e-8
 
    if (p <= 0.0):
        return 0.0
    elif (p >= 1.):
        return 1.;
    elif (a >= 1.0) and (b >= 1.0):
        if (p < 0.5):
            pp = p
        else:
            pp = 1. - p;
        t = math.sqrt(-2.*math.log(pp))
        x = (2.30753+t*0.27061)/(1.0+t*(0.99229+t*0.04481)) - t
        if (p < 0.5):
            x = -x
        al = ((x*x)-3.0)/6.0;
        h = 2.0/(1.0/(2.0*a-1.0)+1.0/(2.0*b-1.0));
        w = (x*math.sqrt(al+h)/h)-(1.0/(2.0*b-1)-1.0/(2.0*a-1.0))*(al+5.0/6.0-2.0/(3.0*h))
        x = a/(a+b*math.exp(2.0*w))
    else:
        lna = math.log(a/(a+b))
        lnb = math.log(b/(a+b))
        t = math.exp(a*lna)/a
        u = math.exp(b*lnb)/b
        w = t + u
        if (p < t/w):
            x = math.pow(a*w*p,1.0/a)
        else:
            x = 1. - math.pow(b*w*(1.0-p),1.0/b)
             
    afac = -math.lgamma(a)-math.lgamma(b)+math.lgamma(a+b)
    j = 0
    for i in range(10):
        if (0.0) or ( x == 1.0):
            return x;
        err = incompbeta(a,b,x) - p
        t = math.exp(a1*math.log(x)+b1*math.log(1.0-x) + afac)
        u = err/t
        t = u/(1.0-0.5*min(1.0,u*(a1/x - b1/(1.0-x))))
        x -= t
        if (x <= 0.):
            x = 0.5*(x + t)
        if (x >= 1.):
            x = 0.5*(x + t + 1.)
        if (math.fabs(t) < ERROR*x) and (j > 0):
            break
    return x
 
##############################################################
################################################################
 
def contfractbeta(a,b,x, ITMAX = 200):
     
    """ contfractbeta() evaluates the continued fraction form of the incomplete Beta function; incompbeta().
    (Code translated from: Numerical Recipes in C.)"""
     
    EPS = 3.0e-7
    bm = az = am = 1.0
    qab = a+b
    qap = a+1.0
    qam = a-1.0
    bz = 1.0-qab*x/qap
     
    for i in range(ITMAX+1):
        em = float(i+1)
        tem = em + em
        d = em*(b-em)*x/((qam+tem)*(a+tem))
        ap = az + d*am
        bp = bz+d*bm
        d = -(a+em)*(qab+em)*x/((qap+tem)*(a+tem))
        app = ap+d*az
        bpp = bp+d*bz
        aold = az
        am = ap/bpp
        bm = bp/bpp
        az = app/bpp
        bz = 1.0
        if (abs(az-aold)<(EPS*abs(az))):
            return az
         
    print( 'a or b too large or given ITMAX too small for computing incomplete beta function.')
 
##################################################################
 
def incompbeta(a, b, x):
     
    ''' incompbeta(a,b,x) evaluates incomplete beta function, here a, b > 0 and 0 <= x <= 1. This function requires contfractbeta(a,b,x, ITMAX = 200)
    (Code translated from: Numerical Recipes in C.)'''
     
    if (x == 0):
        return 0;
    elif (x == 1):
        return 1;
    else:
        lbeta = math.lgamma(a+b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1-x)
        if (x < (a+1) / (a+b+2)):
            return math.exp(lbeta) * contfractbeta(a, b, x) / a;
        else:
            return 1 - math.exp(lbeta) * contfractbeta(b, a, 1-x) / b;
 
 
def t(x, n):
    a = float(n)/float(2)
    b = 0.5
    z = float(n)/float(x**2 + n)
    f = 0.5* (1.0 + sign(x) * float(1.0 - incompbeta(a,b,z)))
    return f