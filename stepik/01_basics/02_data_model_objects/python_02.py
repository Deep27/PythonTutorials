# Python has Mutable and Immutable objects

# --------------------------------------------------------
# |          Immutable            |        Mutable       |
# |------------------------------------------------------|
# | числа (int, float, complex)   | list (x = [1, 2, 3]) |
# | bool                          | dictionary           |
# | tuple (кортеж)                | set                  |
# | string                        |                      |
# | frozenset                     |                      |
# --------------------------------------------------------

objects = [1, 2, 1, 2, 3]
ans = 0
list2 = []

for obj in objects:
    if obj not in list2:
        list2.append(obj)
        ans += 1

print(ans)
