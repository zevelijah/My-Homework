import math
def test_so( val) :
    print(val)
def ThetaPhiMethod1( f, Theta, Phi) :
    fz = (math.sin(Theta))*f
    fu = (math.cos(Theta))*f
    fx = (math.sin(Phi))*fu
    fy = (math.cos(Phi))*fu
    return fx, fy, fz
def cos3Angles(F, Alpha, Beta, Gamma):
    fx = math.cos(Beta) * F
    fy = math.cos(Alpha) * F
    fz = math.cos(Gamma) * F
    return fx, fy, fz
def FindCordAngles(f, fx, fy, fz):
    Alpha1 = math.acos(fx/f)
    Beta1 = math.acos(fy/f)
    Gamma1 = math.acos(fz/f)
    return Alpha1, Beta1, Gamma1
def slopetriangle1(F, a, b, c):
    Fx = a/c*F
    Fy = b/c*F
    return Fx, Fy
def FFromR(r, xr, yr, zr, F):
    fx = F*(xr/r)
    fy = F*(yr/r)
    fz = F*(zr/r)
    return fx, fy, fz
def LegnthThenHeight(f, xr, yr, zr):
    r = math.sqrt((xr**2) + (yr**2) + (zr**2))
    Fx = f*(xr/r)
    Fy = f*(yr/r)
    Fz = f*(zr/r)
    Alpha1 = math.acos(Fx/f)
    Beta1 = math.acos(Fy/f)
    Gamma1 = math.acos(Fz/f)
    return Fx, Fy, Fz, math.degrees(Alpha1), math.degrees(Beta1), math.degrees(Gamma1), r
def cartesionaddition2(ax, ay, az, bx, by, bz):
    rx = ax + bx
    ry = ay + by
    rz = az + bz
    return rx, ry, rz
def cartesionsubtraction(ax, ay, az, bx, by, bz):
    rx = ax + (0-bx)
    ry = ay + (0-by)
    rz = az + (0-bz)
    return rx, ry, rz