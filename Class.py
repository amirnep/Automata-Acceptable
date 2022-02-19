class accept_reject(object):
    def __init__(self):
        self.automata = {}
        self.final = []

    def input(self):
        """Acceptable strings by Automata Written by Amir Nematpour"""
        
        print("Enter States: ")

        states = [i for i in input().split()]

        print("Enter Transitions: ")

        walks = [i for i in input().split()]

        for state in states:
            self.automata[state] = {}
            
            for path in walks:
                fstates = [i for i in input("Enter State to connect to state {} by {}: ".format(state,path)).split()]
                self.automata[state][path] = fstates
                print()

        self.final = [i for i in input("Enter accept states: ").split()]

    def check(self):
        print(self.input.__doc__)
        
        self.input()
        string = [i for i in input("Enter a string: ")]

        state = []
        s = self.automata['0'][string[0]][0]
        state.append(s)

        n = 0
        for i in string[1::]:
            s = self.automata[state[n]][i][0]
            state.append(s)
            n += 1

        e = state.pop()

        if e in self.final:
            return True
        return False
