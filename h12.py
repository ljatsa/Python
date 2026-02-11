#h12.1
#C > F
def tempTeisendamine(t, k):
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