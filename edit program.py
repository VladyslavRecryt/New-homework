import turtle
data = 'string'
data2 = 'getattr'
help(turtle)

for method in dir(turtle):
    print(method)
print(hasattr(data, 'reverse'))
print(hasattr(data, 'index'))
print(getattr(data2, 'startswith'))
print(getattr(data2, 'startswith', None))
print(getattr(data2, 'reverse', None))

