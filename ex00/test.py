#!/usr/bin/env python3
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

# Example 1:
x = [1, 2, 3, 4, 5]
print(ft_map(lambda dum: dum + 1, x))
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different
print(list(ft_map(lambda t: t + 1, x)))
# Output:
# [2, 3, 4, 5, 6]
# Example 2:
print(ft_filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different
print(list(ft_filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]
# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(ft_reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"
print('-' * 30)

function = lambda x: x + 1
iterable = [1, 2, 3]
print(ft_map(function_to_apply = None, iterable = iterable))
try:
    print(list(ft_map(function_to_apply = None, iterable = iterable)))
except Exception as e:
    print(e)
print(ft_filter(function_to_apply = None, iterable = iterable))
print(list(ft_filter(function_to_apply = None, iterable = iterable)))
try:
    print(ft_reduce(None, iterable = iterable))
except Exception as e:
    print(e)
try:
    print(ft_reduce(function, None))
except Exception as e:
    print(e)
print('-' * 30)

print(list(ft_map(lambda x: x + 2, [])))
print(list(ft_map(lambda x: x + 2, [1])))
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
print(list(ft_filter(lambda x: x <= 1, [])))
print(ft_reduce((lambda x, y: x + y), [1]))
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))
