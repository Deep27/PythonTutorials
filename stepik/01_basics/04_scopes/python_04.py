# в телах циклов и условных операторов локальные пространства имен не создаются

for i in range(5):
    x = i * i

print(x)  # Name 'x' can be not defined

for i in []:
    y = i * i
print(y)  # NameError: name 'y' is not defined
