from random import choice
import json
import numpy as np
from itertools import combinations_with_replacement, permutations

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
            # print("CORRECT GUESS!")
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
        return (f"{half_good} half good, {good} good")

def getAllSubsetsWithCertainSum(number_list, target_sum):
    
    matching_numbers = []

    def recursion(subset):
        for number in number_list:
            if sum(subset+[number]) < target_sum:
                recursion(subset+[number])
            elif sum(subset+[number]) == target_sum:
                matching_numbers.append(subset+[number])

    recursion([])
    return matching_numbers

def simpleStrategy(Instance: Game):
    combs = getAllSubsetsWithCertainSum(Instance.color_dict, Instance.pins)
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

g = Game()
simpleStrategy(g)
# g.guess(g.check_input())

# bron https://stackoverflow.com/questions/50239927/find-all-combinations-of-list-elements-including-duplicate-elements
# voor functie "getAllSubsetsWithCertainSum()"