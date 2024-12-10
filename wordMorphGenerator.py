from itertools import product

def wordMorph(s):
    
    lowerCase = [char.lower() for char in s]
    upperCase = [char.upper() for char in s]

    cases = []
    cases.append(lowerCase)
    cases.append(upperCase)

    combination = ["".join(combo) for combo in product(*cases)]

    return combination

print(wordMorph("ab"))