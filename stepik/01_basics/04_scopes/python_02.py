# local -> enclosing -> global -> builtin

def b():
    x = 31

    def a():
        print(x)
    a()


b()  # 31

