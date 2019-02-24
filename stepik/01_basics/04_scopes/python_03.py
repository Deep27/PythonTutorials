def a():
    print(x)  # unresolved reference 'x'


def b():
    x = 31
    a()


# x = 11  # no any errors if line is uncommented
b()  # NameError
