

def A(ro,co,inp1):
    return((ro==0 and (co!=0 and co!=inp1-1)) or ((co==0 or co==inp1-1)and(ro!=0) or ro==inp1//2))

def B(ro,co,inp1):
    return((ro==0 or ro==inp1//2 or ro==inp1-1) and (co!=inp1-1)) or co==0 or (co==inp1-1 and (ro!=0 and ro!=inp1//2 and ro!=inp1-1))

def C(ro,co,inp1):
    return((ro==0 or ro==inp1-1)and(co!=0 and co!=inp1-1)) or (co==0 and (ro!=0 and ro!=inp1-1))or(co==inp1-1 and(ro==1 or ro==inp1-2))

def D(ro,co,inp1):
    return((ro==0 or ro==inp1-1)and(co!=inp1-1))or co==0 or(co==inp1-1 and(ro!=0 and ro!=inp1-1))

def E(ro,co,inp1):
    return(ro==0 or ro==inp1//2 or ro==inp1-1 or co==0)

def F(ro,co,inp1):
    return(ro==0 or ro==inp1//2 or co==0)

def G(ro,co,inp1):
    return((ro==0 or ro==inp1-1)and(co!=0))or(co==0 and(ro!=inp1-1 and ro!=0))or(ro==1 and co==inp1-1)or(ro==inp1//1.56 and co<inp1-1 and co>inp1//2)or(ro>inp1//1.56 and co==inp1-1)

def H(ro,co,inp1):
    return(ro==inp1//2 or co==0 or co==inp1-1)

def I(ro,co,inp1):
    return(ro==0 or ro==inp1-1 or co==inp1//2)

def J(ro,co,inp1):
    return(co==inp1//2 and(ro!=inp1-1))or((ro==0 or (ro==inp1-1 and co!=0))and(co<inp1//2))or(co==0 and ro<=inp1-2 and ro>(inp1//2)+1)

def K(ro,co,inp1):
    return(co==0 or( ro==co+2 and ro>(inp1//2)-1) or ro+co==inp1-3)

def L(ro,co,inp1):
    return(co==0 or ro==inp1-1)

def M(ro,co,inp1):
    return(co==0 or co==inp1-1 or((ro==co or ro+co==inp1)and(ro<=inp1//2)))

def N(ro,co,inp1):
    return(co==0 or co==inp1-1 or co==ro)

def O(ro,co,inp1):
    return(co==0 or co==inp1-1 or ro==0 or ro==inp1-1)and((co!=0 and co!=inp1-1) or (ro!=0 and ro!=inp1-1))

def P(ro,co,inp1):
    return(co==0 or ((ro==0 or ro==inp1//2)and(co!=inp1-1)))or(co==inp1-1 and(ro>0 and ro<inp1//2))

def Q(ro,co,inp1):
    return(((co==0 or co==inp1-2)and(ro<inp1-1 and ro>0)) or ((ro==0 or ro==inp1-1)and(co>0 and co<inp1-2)) or (co==ro and ro>inp1//2))

def R(ro,co,inp1):
    return(co==0 or ((ro==0 or ro==inp1//2)and(co!=inp1-1)))or(co==inp1-1 and(ro>0 and ro<inp1//2))or(ro==co and(ro>inp1//2))

def S(ro,co,inp1):
    return((ro==0 and co!=0)or(ro==inp1//2 and(co!=0 and co!=inp1-1))or(ro==inp1-1 and co!=inp1-1)or(co==0 and(ro>0 and ro<inp1//2))or(co==inp1-1 and(ro>inp1//2 and ro<inp1-1)))

def T(ro,co,inp1):
    return(co==inp1//2 or ro==0)

def U(ro,co,inp1):
    return(co==0 or co==inp1-1 or ro==inp1-1)and(ro!=inp1-1 or (co!=inp1-1 and co!=0))

def V(ro,co,inp1):
    return(co==ro-3 or co+ro==inp1+2)and(ro<inp1-1)

def W(ro,co,inp1):
    return(co==0 or co==inp1-1 or((co==ro or co+ro==inp1)and(ro>=inp1//2)))

def X(ro,co,inp1):
    return(co==ro or co+ro==inp1-1)

def Y(ro,co,inp1):
    return((ro==co or ro+co==inp1-1)and(ro<=inp1//2))or(co==inp1//2 and ro>=inp1//2)

def Z(ro,co,inp1):
    return(ro==0 or ro==inp1-1 or ro+co==inp1-1)

def a(ro,co,inp1):
    return(ro==(inp1//2)-1 or (co==(inp1//2)-1)or ro==inp1-1 or ro==((inp1//2)+(inp1//4))-1 or co==inp1-1)and not(((ro<=((inp1//2)+(inp1//4))-1)and(co==(inp1//2)-1))or(ro<(inp1//2)-1)or(co<(inp1//2)-1)or((ro==inp1-1 or(ro==(inp1//2)-1))and((co==(inp1//2)-1)or(co==inp1-1))))

def b(ro,co,inp1):
    return((co==0 or ro==inp1//2 or ro==inp1-1)and(co!=inp1-1))or(co==inp1-1 and(ro>inp1//2 and ro<inp1-1))

def c(ro,co,inp1):
    return((co==(inp1//2)-3 and (ro>(inp1//2)-2 and ro<inp1-1))or(ro==(inp1//2)-2 or ro==inp1-1)and(co>(inp1//2)-3 and co<inp1-1))or((ro==(inp1//2)-1 or ro==inp1-2)and(co==inp1-1))

def d(ro,co,inp1):
    return(co==inp1-1 or((ro==inp1//2 or ro==inp1-1)and(co!=0))or(co==0 and(ro>inp1//2 and ro<inp1-1)))

def e(ro,co,inp1):
    return(ro==(inp1//2)-1 or ro==inp1-1 or(co==inp1-1) or co==(inp1//2)-1 or ro==((inp1//2)+(inp1//4)-1))and not((co<(inp1//2)-1)or ((ro>(inp1//2)+(inp1//4)-1)and(co==inp1-1)) or(co==inp1-1 and(ro==(inp1//2)-1))or(ro<(inp1//2)-1)or((co==(inp1//2)-1)and(ro==inp1-1 or ro==(inp1//2)-1)))

def f(ro,co,inp1):
    return(ro==0 and co>2) or ro==inp1//2 or (co==2 and ro>0)

def g(ro,co,inp1):
    return(ro==0 and co>=inp1-2)or(ro==inp1//2 and co==0)or((ro==0 or ro==inp1-2 or ro==(inp1//2)-1 or ro==(inp1//2)+1)and(co>0 and co<inp1-3)or((co==0 or co==inp1-3)and ((ro>0 and ro<(inp1//2)-1) or (ro>(inp1//2)+1 and ro<inp1-2))))

def h(ro,co,inp1):
    return(co==0 or (ro==inp1//2 and(co>1 and co<inp1-1)))or(co==inp1-1 and ro>(inp1//2))or(ro==(inp1//2)+1 and co==1)

def i(ro,co,inp1):
    return(co==inp1//2 and(ro>inp1//4))or(ro==(inp1//4)-1 and co==inp1//2)or(ro==inp1-1)or(ro==(inp1//4)+1 and co<inp1//2)

def j(ro,co,inp1):
    return(((ro==inp1-1 and(co<=inp1//2 and co>=0))or(((ro<=inp1-2 and ro>(inp1//2)+1) and(co==0)))or (ro==2 and co<inp1//2) or co==inp1//2))and(not((ro==1)or(ro==inp1-1 and(co==0 or co==inp1//2))))

def k(ro,co,inp1):
    return((co==0 and ro>inp1//4)or(co+1+inp1//2==ro)or(ro+co==inp1-3 and ro>inp1//4))

def l(ro,co,inp1):
    return(co==inp1//2)or(ro==inp1-1)or(ro==0 and co<inp1//2)

def m(ro,co,inp1):
    return((ro==inp1//2 and (co!=(inp1//2) and co!=0 and co!=inp1-1))or((co==0 or co==(inp1//2) or co==inp1-1) and ro>(inp1//2)))

def n(ro,co,inp1):
    return(ro==inp1//2 and(co!=1 and co!=inp1-1))or((co==1 or co==inp1-1)and ro>inp1//2)

def o(ro,co,inp1):
    return((ro==(inp1//2)-1 or ro==inp1-1 or co==(inp1//2)-1 or co==inp1-1))and not(((ro==(inp1//2)-1 or ro==inp1-1)and(co==(inp1//2)-1 or co==inp1-1))or((co<(inp1//2)-1)or(ro<(inp1//2)-1)))

def p(ro,co,inp1):
    return((co==(inp1//2)-1)) or ((ro==0 or ro==inp1//2)and(co!=inp1-1 and co>(inp1//2)-1))or(co==inp1-1 and(ro>0 and ro<inp1//2))

def q(ro,co,inp1):
    return((co==inp1-1 or (co==0 and ro<inp1//2)) and ro>=(inp1//2)-3)or((ro==inp1//2 or ro==0) and co!=0)

def r(ro,co,inp1):
    return(co==0 and ro>=(inp1//2)-1)or((ro==(inp1//2)-1 and(co!=1)))or((co==1) and ro==inp1//2)

def s(ro,co,inp1):
    return(co==0 and ro>(inp1//3)-1 and ro<inp1-1-(inp1//3))or((ro==(inp1//3)-1 or ro==inp1-1-inp1//3 or ro==inp1-1) and co!=0 and co!=inp1-1)or(ro==(inp1//3) and co==0)or(co==inp1-1 and(ro<inp1-1 and ro>inp1-1-(inp1//3)))

def t(ro,co,inp1):
    return(co==inp1//2 and ro!=inp1-1)or(ro==(inp1//2)-1)or(ro==inp1-1 and co>inp1//2)

def u(ro,co,inp1):
    return(ro==inp1-1 or co==(inp1//2)-1 or co==inp1-1)and not((ro==inp1-1 and(co==(inp1//2)-1 or co==inp1-1))or((ro<(inp1//2)-1)or(co<(inp1//2)-1)))

def v(ro,co,inp1):
    return(co==ro-3 or co+ro==inp1+2)and(ro<inp1-1)

def w(ro,co,inp1):
    return((ro==inp1-1 and (co!=(inp1//2) and co!=0 and co!=inp1-1))or((co==0 or co==(inp1//2) or co==inp1-1) and ro<inp1-1 and ro>=(inp1//2)))

def x(ro,co,inp1):
    return((ro==co and ro>inp1//5) or ro+co==inp1+1)

def y(ro,co,inp1):
    return((ro+co==inp1-1)or(ro==co and ro<inp1//2))

def z(ro,co,inp1):
    return(co+ro==inp1+2 or ((ro==(inp1//2)-1 or ro==inp1-1)and(co>(inp1//2)-1)))

