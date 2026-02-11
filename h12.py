#h12.1
#C > F
def tempTeisendamine(t, k):
    """
    Teisendab C > F või F > C.
    Parameetrid:
    a (int): Text.
    b (int): Teine arv.

    Tagastab:
    Prindib vastuse

    Näide:
    >>> tempTeisendamine("c", 19.445)
    5
    """
    if t == "c":
        vastus = k * 9/5 + 32
    elif t == "f":
        vastus = (k - 32) / (9/5)
    else:
        #ei saanud aru
        vastus = "Ma ei mõista sind"
    print(vastus)

tempTeisendamine("c", 19.445)
tempTeisendamine("f", 19.445)
tempTeisendamine("blablabla", 19.445)
print(tempTeisendamine.__doc__)

#12.2
#5L/100
#L * KM/100

kytus = lambda x, y: x * y/100
print(kytus( 5, 150))

#12.3
#pank depo ja väljavõte
def depo(s, r):
    """
    Docstring for depo
    """
    uus = s + r
    return uus

def vv(s, r):
        """
    Docstring for vv
         """
    uus = s - r
    return uus

    saldo = 100

    print(saldo)
    saldo = depo(saldo, 10)
    saldo = depo(saldo, 100)
    saldo = depo(saldo, 1000)
    saldo = depo(saldo, 15)
    saldo = depo(saldo, 1)
    print(saldo)
    saldo = vv (saldo, 100)
    saldo = vv (saldo, 100)
    saldo = vv (saldo, 100)
    saldo = vv (saldo, 100)
    saldo = vv (saldo, 100)
    print(saldo)