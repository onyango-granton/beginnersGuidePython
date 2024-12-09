def sumRange(num):
    if num == 0:
        return 0
    else:
        return num + sumRange(num - 1)
    
def addList(lst):
    if not lst:
        return 0
    else:
        return lst[0] + addList(lst[1:])
    
def inverseChristmasTree(stars, spacing):
    if stars == 1:
        return " " * (spacing-stars) + "*"
    else:
        return " " * (spacing-stars) +"* " * stars + "\n" + inverseChristmasTree(stars - 1, spacing)
    
def uprightChristmasTree(stars, startPoint, spacing):
    if startPoint == stars:
        return " " * (spacing-startPoint) +"* " * stars
    else:
        return " " * (spacing-startPoint) +"* " * startPoint +"\n" + uprightChristmasTree(stars, startPoint+1, spacing)
    
print(uprightChristmasTree(5,1,5))