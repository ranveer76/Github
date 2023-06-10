def pr():
    global x2, ro, co, oup
    for co in range(inp1):
        if (d[x2]()):
            print('*', end='')
        else:
            print(' ', end='')


def sp():
    for co in range(inp1//2):
        print(' ', end='')


def A():
    return ((ro == 0 and (co != 0 and co != inp1-1)) or ((co == 0 or co == inp1-1) and (ro != 0) or ro == inp1//2))


def B():
    return ((ro == 0 or ro == inp1//2 or ro == inp1-1) and (co != inp1-1)) or co == 0 or (co == inp1-1 and (ro != 0 and ro != inp1//2 and ro != inp1-1))


def C():
    return ((ro == 0 or ro == inp1-1) and (co != 0 and co != inp1-1)) or (co == 0 and (ro != 0 and ro != inp1-1)) or (co == inp1-1 and (ro == 1 or ro == inp1-2))


def D():
    return ((ro == 0 or ro == inp1-1) and (co != inp1-1)) or co == 0 or (co == inp1-1 and (ro != 0 and ro != inp1-1))


def E():
    return (ro == 0 or ro == inp1//2 or ro == inp1-1 or co == 0)


def F():
    return (ro == 0 or ro == inp1//2 or co == 0)


def G():
    return ((ro == 0 or ro == inp1-1) and (co != 0)) or (co == 0 and (ro != inp1-1 and ro != 0)) or (ro == 1 and co == inp1-1) or (ro == inp1//1.56 and co < inp1-1 and co > inp1//2) or (ro > inp1//1.56 and co == inp1-1)


def H():
    return (ro == inp1//2 or co == 0 or co == inp1-1)


def I():
    return (ro == 0 or ro == inp1-1 or co == inp1//2)


def J():
    return (co == inp1//2 and (ro != inp1-1)) or ((ro == 0 or (ro == inp1-1 and co != 0)) and (co < inp1//2)) or (co == 0 and ro <= inp1-2 and ro > (inp1//2)+1)


def K():
    return (co == 0 or (ro == co+2 and ro > (inp1//2)-1) or ro+co == inp1-3)


def L():
    return (co == 0 or ro == inp1-1)


def M():
    return (co == 0 or co == inp1-1 or ((ro == co or ro+co == inp1) and (ro <= inp1//2)))


def N():
    return (co == 0 or co == inp1-1 or co == ro)


def O():
    return (co == 0 or co == inp1-1 or ro == 0 or ro == inp1-1) and ((co != 0 and co != inp1-1) or (ro != 0 and ro != inp1-1))


def P():
    return (co == 0 or ((ro == 0 or ro == inp1//2) and (co != inp1-1))) or (co == inp1-1 and (ro > 0 and ro < inp1//2))


def Q():
    return (((co == 0 or co == inp1-2) and (ro < inp1-1 and ro > 0)) or ((ro == 0 or ro == inp1-1) and (co > 0 and co < inp1-2)) or (co == ro and ro > inp1//2))


def R():
    return (co == 0 or ((ro == 0 or ro == inp1//2) and (co != inp1-1))) or (co == inp1-1 and (ro > 0 and ro < inp1//2)) or (ro == co and (ro > inp1//2))


def S():
    return ((ro == 0 and co != 0) or (ro == inp1//2 and (co != 0 and co != inp1-1)) or (ro == inp1-1 and co != inp1-1) or (co == 0 and (ro > 0 and ro < inp1//2)) or (co == inp1-1 and (ro > inp1//2 and ro < inp1-1)))


def T():
    return (co == inp1//2 or ro == 0)


def U():
    return (co == 0 or co == inp1-1 or ro == inp1-1) and (ro != inp1-1 or (co != inp1-1 and co != 0))


def V():
    return (co == ro-3 or co+ro == inp1+2) and (ro < inp1-1)


def W():
    return (co == 0 or co == inp1-1 or ((co == ro or co+ro == inp1) and (ro >= inp1//2)))


def X():
    return (co == ro or co+ro == inp1-1)


def Y():
    return ((ro == co or ro+co == inp1-1) and (ro <= inp1//2)) or (co == inp1//2 and ro >= inp1//2)


def Z():
    return (ro == 0 or ro == inp1-1 or ro+co == inp1-1)


def a():
    return (ro == (inp1//2)-1 or (co == (inp1//2)-1) or ro == inp1-1 or ro == ((inp1//2)+(inp1//4))-1 or co == inp1-1) and not (((ro <= ((inp1//2)+(inp1//4))-1) and (co == (inp1//2)-1)) or (ro < (inp1//2)-1) or (co < (inp1//2)-1) or ((ro == inp1-1 or (ro == (inp1//2)-1)) and ((co == (inp1//2)-1) or (co == inp1-1))))


def b():
    return ((co == 0 or ro == inp1//2 or ro == inp1-1) and (co != inp1-1)) or (co == inp1-1 and (ro > inp1//2 and ro < inp1-1))


def c():
    return ((co == (inp1//2)-3 and (ro > (inp1//2)-2 and ro < inp1-1)) or (ro == (inp1//2)-2 or ro == inp1-1) and (co > (inp1//2)-3 and co < inp1-1)) or ((ro == (inp1//2)-1 or ro == inp1-2) and (co == inp1-1))


def d():
    return (co == inp1-1 or ((ro == inp1//2 or ro == inp1-1) and (co != 0)) or (co == 0 and (ro > inp1//2 and ro < inp1-1)))


def e():
    return (ro == (inp1//2)-1 or ro == inp1-1 or (co == inp1-1) or co == (inp1//2)-1 or ro == ((inp1//2)+(inp1//4)-1)) and not ((co < (inp1//2)-1) or ((ro > (inp1//2)+(inp1//4)-1) and (co == inp1-1)) or (co == inp1-1 and (ro == (inp1//2)-1)) or (ro < (inp1//2)-1) or ((co == (inp1//2)-1) and (ro == inp1-1 or ro == (inp1//2)-1)))


def f():
    return (ro == 0 and co > 2) or ro == inp1//2 or (co == 2 and ro > 0)


def g():
    return (ro == 0 and co >= inp1-2) or (ro == inp1//2 and co == 0) or ((ro == 0 or ro == inp1-2 or ro == (inp1//2)-1 or ro == (inp1//2)+1) and (co > 0 and co < inp1-3) or ((co == 0 or co == inp1-3) and ((ro > 0 and ro < (inp1//2)-1) or (ro > (inp1//2)+1 and ro < inp1-2))))


def h():
    return (co == 0 or (ro == inp1//2 and (co > 1 and co < inp1-1))) or (co == inp1-1 and ro > (inp1//2)) or (ro == (inp1//2)+1 and co == 1)


def i():
    return (co == inp1//2 and (ro > inp1//4)) or (ro == (inp1//4)-1 and co == inp1//2) or (ro == inp1-1) or (ro == (inp1//4)+1 and co < inp1//2)


def j():
    return (((ro == inp1-1 and (co <= inp1//2 and co >= 0)) or (((ro <= inp1-2 and ro > (inp1//2)+1) and (co == 0))) or (ro == 2 and co < inp1//2) or co == inp1//2)) and (not ((ro == 1) or (ro == inp1-1 and (co == 0 or co == inp1//2))))


def k():
    return ((co == 0 and ro > inp1//4) or (co+1+inp1//2 == ro) or (ro+co == inp1-3 and ro > inp1//4))


def l():
    return (co == inp1//2) or (ro == inp1-1) or (ro == 0 and co < inp1//2)


def m():
    return ((ro == inp1//2 and (co != (inp1//2) and co != 0 and co != inp1-1)) or ((co == 0 or co == (inp1//2) or co == inp1-1) and ro > (inp1//2)))


def n():
    return (ro == inp1//2 and (co != 1 and co != inp1-1)) or ((co == 1 or co == inp1-1) and ro > inp1//2)


def o():
    return ((ro == (inp1//2)-1 or ro == inp1-1 or co == (inp1//2)-1 or co == inp1-1)) and not (((ro == (inp1//2)-1 or ro == inp1-1) and (co == (inp1//2)-1 or co == inp1-1)) or ((co < (inp1//2)-1) or (ro < (inp1//2)-1)))


def p():
    return ((co == (inp1//2)-1)) or ((ro == 0 or ro == inp1//2) and (co != inp1-1 and co > (inp1//2)-1)) or (co == inp1-1 and (ro > 0 and ro < inp1//2))


def q():
    return ((co == inp1-1 or (co == 0 and ro < inp1//2)) and ro >= (inp1//2)-3) or ((ro == inp1//2 or ro == 0) and co != 0)


def r():
    return (co == 0 and ro >= (inp1//2)-1) or ((ro == (inp1//2)-1 and (co != 1))) or ((co == 1) and ro == inp1//2)


def s():
    return (co == 0 and ro > (inp1//3)-1 and ro < inp1-1-(inp1//3)) or ((ro == (inp1//3)-1 or ro == inp1-1-inp1//3 or ro == inp1-1) and co != 0 and co != inp1-1) or (ro == (inp1//3) and co == 0) or (co == inp1-1 and (ro < inp1-1 and ro > inp1-1-(inp1//3)))


def t():
    return (co == inp1//2 and ro != inp1-1) or (ro == (inp1//2)-1) or (ro == inp1-1 and co > inp1//2)


def u():
    return (ro == inp1-1 or co == (inp1//2)-1 or co == inp1-1) and not ((ro == inp1-1 and (co == (inp1//2)-1 or co == inp1-1)) or ((ro < (inp1//2)-1) or (co < (inp1//2)-1)))


def v():
    return (co == ro-3 or co+ro == inp1+2) and (ro < inp1-1)


def w():
    return ((ro == inp1-1 and (co != (inp1//2) and co != 0 and co != inp1-1)) or ((co == 0 or co == (inp1//2) or co == inp1-1) and ro < inp1-1 and ro >= (inp1//2)))


def x():
    return ((ro == co and ro > inp1//5) or ro+co == inp1+1)


def y():
    return ((ro+co == inp1-1) or (ro == co and ro < inp1//2))


def z():
    return (co+ro == inp1+2 or ((ro == (inp1//2)-1 or ro == inp1-1) and (co > (inp1//2)-1)))


tinp = int(input('Enter 1 for horizontal pattern or 2 for vertical:\n'))
print('enter 1 for all uppercase:\n', '2 for all lowercase:\n',
      '3 for all vowels:\n', '4 for printing desired alphabet')
ti = int(input())
d = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z,
     'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f, 'g': g, 'h': h, 'i': i, 'j': j, 'k': k, 'l': l, 'm': m, 'n': n, 'o': o, 'p': p, 'q': q, 'r': r, 's': s, 't': t, 'u': u, 'v': v, 'w': w, 'x': x, 'y': y, 'z': z}
inp = input('Enter Any Word:')
if ti == 1:
    inp = inp.upper()
elif ti == 2:
    inp = inp.lower()
elif ti == 3:
    d = {'A': A, 'E': E, 'I': I, 'O': O, 'U': U,
         'a': a, 'e': e, 'i': i, 'o': o, 'u': u}
elif ti == 4:
    x3 = input('enter alhphabet you want to print from word:')[0]
inp1 = 9
le = len(inp)
if tinp == 1:
    inp = inp.split()
    for oupx in inp:
        for ro in range(inp1):
            for oup in oupx:
                if ti != 4:
                    x3 = oup
                if oup in d and x3 == oup:
                    x2 = oup
                    sp()
                    pr()
            print()
        print()
elif tinp == 2:
    for oup in range(le):
        print()
        for ro in range(inp1):
            if ti != 4:
                x3 = inp[oup]
            if inp[oup] in d and x3 == inp[oup]:
                x2 = inp[oup]
                pr()
            print()
input('press enter to exit')
