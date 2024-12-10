from itertools import product

def wordMorph(s):
    combinations = []
    '''for x in s:
        currentChar = []
        currentChar.append(x.lower())
        currentChar.append(x.upper())
        combinations.append(currentChar)'''

    combinations = [[x.lower(), x.upper()] for x in s]

    letterCombo = ["".join(x) for x in product(*combinations)]

    return letterCombo

print(wordMorph("ab"))