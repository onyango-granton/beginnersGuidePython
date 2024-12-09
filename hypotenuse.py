import math

def line_length(dot1, dot2):
    height = abs(dot1[0]-dot2[0])
    base = abs(dot1[1]-dot2[1])
    return round(math.sqrt(height*height + base * base),2)

print(line_length([15, 7], [22, 11]))