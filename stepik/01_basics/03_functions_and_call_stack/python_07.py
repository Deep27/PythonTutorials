# def function_name([positional_args,                   # EXAMPLE AT THE BOTTOM
#                   [positional_args_with_default,
#                   [*pos_args_name,
#                   [keyword_only_args,  # rarely used
#                   [**kw_args_name]]]]]):
#
# CORRECT
def printab(a, b):  # function with 2 positional arguments
    print(a)
    print(b)


def printab2(a, b=10):  # one of arguments has a default value
    print(a)
    print(b)


def printab3(a=10, b=10):  # both arguments have a default value
    print(a)
    print(b)

# INCORRECT
# def printab4(a=10, b):  # non-default arguments follows default argument
#     print(a)
#     print(b)


def printab4(a, b, *args):
    print("positional argument a ", a)
    print("positional argument b ", b)
    print("additional arguments: ")
    for arg in args:
        print(arg)


printab4(10, 20, 30, 40, 50)


def printab5(a, b, **kwargs):
    print("positional argument a ", a)
    print("positional argument b ", b)
    print("additional arguments: ")
    for key in kwargs:
        print(key, kwargs[key])


printab5(10, 20, c=30, d=40, jimmi=123)
printab5(10, c=30, d=40, jimmi=123, b=20)


def printab6(a, b=10, *args, c=10, d, **kwargs):
    print(a, b, c, d)


printab6(15, d=15)
