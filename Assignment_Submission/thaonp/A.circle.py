import math
from turtle import *
color('green','yellow')
begin_fill()
i=0
while i<=360:
    right(1)
    forward( 1000 * math.pi / 360 )
    i=i+1
end_fill()
