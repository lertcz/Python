class NotInAlphabet(Exception):
    pass

class TransitionNotFound(Exception):
    pass

class NotDeterministic(Exception):
    pass 

DEBUG = False
def debug(str):
        if DEBUG:
            print(str)

class Simulation():
    def __init__(self, Start, Finish, Sigma):
        self.Start = Start
        self.Finish = Finish
        self.Sigma = Sigma
        self.Current = ""
    
    def findStart(self, states):
        for node in states:
            if node == self.Start:
                self.Current = node
                return
    
    def isDeterministic(self, data):
        Transitions = []
        for node in data["Nodes"]:
            current = node["Start"]
            condition = node["Cond"]

            element = current + condition
            if element in Transitions:
                return False
            else:
                Transitions.append(element)
        return True
    
    def deterministic(self, data, Input):
        if self.isDeterministic(data):
            self.iterate(Input, self.Sigma, data)
        else:
            raise NotDeterministic("the automata is not deterministic")
    
    def iterate(self, Input, Sigma, data):
        for char in Input:
            if char not in Sigma: # check if char is in sigma
                raise NotInAlphabet("char is not included in sigma")

            found = False # variable for checking if the transition happened

            for node in data["Nodes"]:
                #init variables for clarity
                current = node["Start"]
                condition = node["Cond"]
                next = node["End"]

                if self.Current == current and condition == char: # check if the code is on current node and condition is true
                    self.Current = next
                    found = True
                    debug(next)
                    break
            
            if not found: # check if the transition didn't pass
                raise TransitionNotFound(f"Transition from state: {self.Current} with cond: {char} not found!")

    def checkEndState(self): # check if the automata ended on finish node
        return self.Current in self.Finish

        #if self.Current == self.Finish:
        #    return True
        #else: 
        #    return False

    def detectEpsilon(self, data):
        for node in data["Nodes"]:
            condition = node["Cond"]
            if condition == "":
                return [True, node["Start"], node["End"]]
        return False

    def epsilonRemoval(self, data):
        detected, node1, node2 = self.detectEpsilon(data)

        if detected:
            print(f"epsilon: {node1}, {node2}")

            return True
        
        else:
            return False


    def simulate(self, states, Input, data):
        self.findStart(states)
        #while self.epsilonRemoval(data): pass
        self.deterministic(data, Input)
        return self.checkEndState()

        
