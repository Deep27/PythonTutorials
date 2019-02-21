# пространства имен:
#     builtins: int, str, float, bool
#                 min, max, abs
#     main: a = 1
#             def fun(...):
#                 ...
#                 x = 1  # в локальном namespace функции fun

t_c = 18  # global
tmp = "ok"  # global


def fahrenheit(t_c):  # global # shadows t_c from outer scope
    tmp = t_c * 9 / 5  # local # shadows tmp from outer scope # tmp ? fun_namespace ? yes
    return tmp + 32


print(fahrenheit(t_c))  # global ? no -> builtins ? yes
print(tmp)  # global ? no -> builtins ? yes
