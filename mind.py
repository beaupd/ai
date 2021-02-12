from random import choice
import datetime

# possibilities: pawns**2 * colors

# De class voor de game instance
class Mastermind:
    _colors = {'blauw', 'geel', 'groen', 'oranje', 'rood', 'zwart'}
    _pawns = 4
    _slots = range(_pawns)

    def __init__(self):
        # print(self._colors)
        self.color_dict = dict(zip([i for i in range(len(self._colors))], self._colors))

    #def feedback():
        # 0 == almost
        # 1 == good
        # in list if not list feedback == false

    def init_nGUI(self): # De game zonder graphical user interface
        print("########---------#########\nMastermind\n")
        while 1:
            try:
                random_in = int(input("Do you want to put in Code yourself?\n1: yes / 0: no\n"))
                break
            except:
                print("wrong input try again")
                continue
        if random_in:
            code_in = self.check_input()
            self.code = [self.color_dict[int(i)] for i in code_in]
        else:
            self.code = [choice(self.color_dict) for _ in self._slots]
        
    def check_input(self):
        while 1:
            try:
                print(f"Put in the index of the color amount of indexes:{self._pawns}, this is the dict:\n{self.color_dict}")
                code_in = str(input())
                if len(code_in) != self._pawns:
                    raise Exception
                else:
                    for c in code_in:
                        int(c) # check if number if int conversion is error than exception is raised
                        if int(c) > len(self.color_dict)-1:
                            raise Exception
                return code_in
            except:
                print("wrong input, try again")
                continue

    def play_input(self, limit=None):
        self.playing = True
        if limit == None:
            while 1 and self.playing:
                self.doRound()
        else:
            index = limit
            while index > 0 and self.playing:
                index-= 1
                self.doRound()
                print("round")
            if self.playing == True:
                print("out of rounds ;(",f"Correct answer was {self.code}")

    def doRound(self):
        guess = [self.color_dict[int(i)] for i in self.check_input()]
        half_good = 0
        good = 0
        if guess == self.code:
            self.playing = False
            print("CORRECT GUESS!")
            return
        for i, c in enumerate(self.code):
            if c in guess:
                if i == guess.index(c):
                    good += 1
                else:
                    half_good += 1
        print(half_good, good)
    
# def simple_strategy():


# print(sorted(["zwart", "groen", "oranje", "rood", "blauw", "geel"]))
m = Mastermind()
m.init_nGUI()
m.play(10)
# print(m.color_dict)

    
