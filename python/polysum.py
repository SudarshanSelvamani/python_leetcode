import math
def polysum(n, s): # n = number of sides , s = size of a side 
    return round((0.25*n*s*s/math.tan(math.pi/n))+((n*s)**2),4) #round() rounds the float to given no of digits
# 0.25*n*s*s/math.tan(math.pi/n) = area | (n*s)**2 = square of perimeter | 4 = no of decimal places you want your answer to be