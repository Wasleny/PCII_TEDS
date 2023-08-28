import math

x, y, z = input().split(' ')
x, y, z = int(x), int(y), int(z)

if (z ** 2 + y ** 2 == x ** 2) or (x ** 2 + y ** 2 == z ** 2) or (z ** 2 + x ** 2 == y ** 2):
    print("AREA = {}".format(int(((3 * (z/2)**2) // 2) + ((y * z) // 2))))
else:
    print("Nao eh retangulo!")