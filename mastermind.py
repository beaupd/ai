from random import choice
import json
import numpy as np
from itertools import combinations_with_replacement, permutations, chain

class Game:

    _config = {
        "colors": {'blauw', 'geel', 'groen', 'oranje', 'rood', 'zwart'},
        "pins": 4,
        "manual": False,
        "limit": 10,
    }

    def __init__(self, config=_config):
        self.colors = config["colors"]
        self.pins = config["pins"]
        self.limit = config["limit"]
        self.guesses = 0
        self.playing = True

        self.color_dict = dict(zip([i for i in range(len(self.colors))], self.colors))
        # print(self.color_dict, self.colors)
        if config["manual"]: # Als manual dan wait for (correct) input
            self.code = self.check_input() # call input function
            self.code_words = [self.color_dict[int(i)] for i in self.code] # code omgezet in de naam van de kleur
        else: # als niet manual random code
            self.code = [choice([i for i in range(config["pins"])]) for _ in range(config["pins"])] # random code
            self.code_words = [self.color_dict[int(i)] for i in self.code] # code omgezet in de naam van de kleur

    def check_input(self):
        # try:
        print(f"Put in the {self.pins} colored code, this is the dict:\n{self.color_dict}")
        code_in = str(input())
        if len(code_in) != self.pins:
            raise Exception
        else:
            for c in code_in:
                int(c) # check if number if int conversion is error than exception is raised
                if int(c) > len(self.color_dict)-1:
                    raise Exception
        return code_in
        # except:
        #     print("wrong input, try again")

    def guess(self, code):
        guess = [int(c) for c in code] #[self.color_dict[int(i)] for i in code]
        self.guesses += 1
        half_good = 0
        good = 0
        temp_code = [int(c) for c in self.code]
        blacklist = []
    
        if guess == self.code:
            self.playing = False
            print("CORRECT GUESS!")
            return "CORRECT GUESS!"
        for i in range(self.pins):
            # print(str(guess[i]) ,temp_code[i])
            if guess[i] == temp_code[i]:
                good += 1
                blacklist.append(i)
        for i in range(self.pins):
            if guess[i] in temp_code:
                for idx in range(len(temp_code)):
                    if idx not in blacklist:
                        if guess[i] == temp_code[idx]:
                            half_good += 1
        # print(f"{half_good} half good, {good} good")
        return {"halfGood": half_good, "good": good}


def createPossibleCodes(colors, numberOfPositions):
    return addColor([], colors, numberOfPositions, 0)

def addColor(codeList,colors,numberOfPositions,depth):    
    depth +=1
    # The start of the list with one element
    if len(codeList) == 0:
        for color in colors:            
            codeList.append([color])
    # Add an elememt to the combination
    else:
        for code in codeList:
            for color in colors:               
                code.append(color)
    # recursive
    if (depth < numberOfPositions):        
        codeList = addColor(codeList,colors,numberOfPositions,depth)
    return codeList

def simpleStrategy(Instance: Game):
    combs = createPossibleCodes(Instance.color_dict, Instance.pins)
    print(combs)
    # print(combs, len(combs))
    playing = True
    index = 0
    for c in combs:
        if Instance.playing:
            guess = ''.join(map(str, c))
            print(Instance.guess(guess))
            index+=1
            playing = Instance.playing
    print("end")


def heuristiek(Inst: Game):
    """
        test eerst alle kleuren een het aantal goede, 
        vanuit daar probeert die alle mogelijkheden
        Beau Dekker
    """
    potential = [i for i in Inst.color_dict]
    correct = []
    
    
    for c in potential: # check which colors are in the code and by which amount
        res = g.guess([c for _ in range(Inst.pins)])
        if res["good"] > 0:
            correct.append((c, res["good"]))

    possibles = sum([[c[0] for _ in range(c[1])] for c in correct], []) # get all colors and their amount in code
    for p in [each_permutation for each_permutation in permutations(possibles, 4)]:# Make all possible combinations  (bron 1)
        if Inst.playing:
            res = Inst.guess(p)
        else:
            break

    print(Inst.guesses)


g = Game()
# simpleStrategy(g)
# g.guess(g.check_input())
heuristiek(g)

# bron 1
# all_combinations = [list(zip(each_permutation, list2)) for each_permutation in itertools.permutations(list1, len(list2))]
# https://www.codegrepper.com/code-examples/delphi/all+possible+unique+combinations+of+numbers+from+the+list+python
