from math import cos, pi


def lerp(a, b, t):
    r = a * (1. - t) + b * t
    return r


def cos_interp(a, b, t):
    ft = t * pi
    f = (1. - cos(ft)) * 0.5
    return a*(1.-f) + b*f


def cubic_interp(v0, v1, v2, v3, x):
    v0v1 = v0 - v1
    p = (v3 - v2) - v0v1
    q = v0v1 - p
    r = v2 - v00
    s = v1
    xxx = x*x*x
    xx = x*x
    return p*xxx + q*xx + r*x + s


def bilerp(v00, v01, v10, v11, t0, t1, fn_interp=lerp):
    r0 = fn_interp(v00, v01, t0)
    r1 = fn_interp(v10, v11, t0)
    r = fn_interp(r0, r1, t1)
    return r
