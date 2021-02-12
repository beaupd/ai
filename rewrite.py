from random import choice
import json
import numpy as np
from itertools import permutations 

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
        print(self.color_dict, self.colors)
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
        temp_code = self.code
    
        if guess == self.code:
            self.playing = False
            # print("CORRECT GUESS!")
            return "CORRECT GUESS!"
        for i, c in enumerate(guess):
            print(c, guess, self.code)
            if c in temp_code:
                if c == self.code[i]:
                    temp_code[i] = len(self.colors)+1 # zet index naar een onbereikbaar getal zodat we geen dubbele goeds of half goods krijgen
                    good += 1
                else:
                    half_good += 1
        return (f"{half_good} half good, {good} good")

def simpleStrategy(Instance: Game):
    combs = list(permutations(Instance.color_dict, Instance.pins))
    playing = True
    index = 0
    while playing:
        guess = ''.join(map(str, combs[index]))
        print(guess, Instance.guess(guess))
        index+=1
        playing = Instance.playing
    print("end")

g = Game()
simpleStrategy(g)
