from itertools import product

def letterCombination(digit):
    listCombo = []
    combination = [] 
    digitLetter = {
        2 : ["a","b","c"],
        3 : ["d","e","f"],
        4 : ["g","h","i"],
        5 : ["j","k","l"],
        6 : ["m","n","o"],
        7 : ["p","q","r", "s"],
        8 : ["t","u","v"],
        9 : ["w","x","y", "z"],
    }
    if digit == "":
        return []
    for x in digit:
        listCombo.append(digitLetter[int(x)])
       
    for x in product(*listCombo):
        combination.append("".join(x))

   # combination = ["".join(combo) for combo in product(*listCombo)]
    return combination

print(letterCombination("2"))