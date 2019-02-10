def list_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result


def my_sum(a, b):
    return a + b


y = my_sum(14, 29)
z = list_sum([1, 2, 3])
print(y)
print(z)
