from random import choice
import datetime

# possibilities: pawns**2 * colors

# De class voor de game instance
class Mastermind:
    _colors = set({'blauw', 'geel', 'groen', 'oranje', 'rood', 'zwart'})
    _pawns = 4
    _slots = range(_pawns)

    def __init__(self):
        # print(self._colors)
        self.color_dict = dict(zip([i for i in range(len(self._colors))], self._colors))
        self.no_GUI()

    #def feedback():
        # 0 == almost
        # 1 == good
        # in list if not list feedback == false

    def no_GUI(self):
        print("########---------#########\nMastermind\n")
        while 1:
            try:
                random_in = int(input("Do you want to put in Code yourself?\n1: yes / 0: no\n"))
                break
            except:
                print("wrong input try again")
                continue
        if random_in:
            print("This is the color dict:",self.color_dict,f"Put in a {self._pawns} colored code corresponding with the numbers\n")
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

    def play(self, limit=None):
        if limit == None:
            infinite = True
        else:
            infinite = False

        if infinite:
            while 1:
                self.doRound()
        else:
            self.doRound()
            print("out of rounds ;(")

    def doRound(self):
        guess = self.check_input()
        
        for c in self.code:
            if c in guess:

# print(sorted(["zwart", "groen", "oranje", "rood", "blauw", "geel"]))
m = Mastermind()
# print(m.color_dict)

    
