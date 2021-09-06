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
    
    """ def findStart(self, states):
        for node in states:
            if node == self.Start:
                self.Current = node
                return """
    
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
                #TODO fix if transition does not exist!!!
                print(len(data["Start"]))
                if len(data["Start"]) == 1:
                    raise TransitionNotFound(f"Transition from state: {self.Current} with cond: {char} not found!")
                else: return

    def checkEndState(self): # check if the automata ended on finish node
        return self.Current in self.Finish

        #if self.Current == self.Finish:
        #    return True
        #else: 
        #    return False

    def detectEpsilon(self, data):
        global transitionPos
        transitionPos = 0
        for node in data["Nodes"]:
            condition = node["Cond"]
            if condition == "":
                return [True, node["Start"], node["End"]]
            transitionPos += 1
        return [False, "", ""]

    def epsilonRemoval(self, data):
        detected, node1, node2 = self.detectEpsilon(data)

        if detected:
            debug(f"epsilon transition nodes: {node1}, {node2}")
            node2Cond, node2End, node2EndPos = [], [], []

            #find all outgoing transitions from node2
            position = 0
            for node in data["Nodes"]:
                if node["Start"] == node2:
                    node2Cond.append(node["Cond"])
                    node2End.append(node["End"])
                    node2EndPos.append(position)
                position += 1
            
            debug(node2Cond + node2End + node2EndPos)

            # delete the epsilon transition
            del data["Nodes"][transitionPos]
            debug(f"deleted epislon transition: {transitionPos}")

            #assign the transitions
            for x in range(len(node2Cond)):
                nodeData = {
                    "Start" : f"{node1}",
                    "Cond" : f"{node2Cond[x]}",
                    "End" : f"{node2End[x]}"
                }
                data["Nodes"].insert(node2EndPos[x], nodeData)

            #add nodes in start or finish variables if needed
            if node1 in data["Start"]:
                data["Start"].append(node2)
                self.Finish = data["Start"]
            
            if node2 in data["Finish"]:
                data["Finish"].append(node1)
                self.Finish = data["Finish"]
            
            #print(data["Start"], data["Finish"])


            return True # !change to True 
        
        else:
            return False

    def runAllStarts(self, data, Input):
        for start in data["Start"]:
            #set the start
            self.Current = start
            #check if the automat is deterministic
            self.deterministic(data, Input)
            return self.checkEndState()

    def simulate(self, Input, data):
        while self.epsilonRemoval(data): pass
        return self.runAllStarts(data, Input)

        
