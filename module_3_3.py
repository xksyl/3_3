def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(a=5, b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = [10, 'список', False]
values_dict = {'a': 55, 'b': 'словарь', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'второй']
print_params(*values_list_2, 42)


