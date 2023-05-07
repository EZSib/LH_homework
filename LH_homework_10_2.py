from math import *

a = 32 / (sin(-35*pi/4) * cos(25 * pi/4))
b = 24 / (sin(radians(127)) ** 2 +1 + sin(radians(217)))
c = sqrt(48) - sqrt(192) * (sin( 19 * pi / 12)) ** 2
d = 7 * (sin(radians(11))) / cos(radians(79))
print(*(list(map(lambda x: round(x, 2), (a, b, c, d)))), sep='\n')
