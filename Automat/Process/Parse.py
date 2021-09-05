class Parse():
    def __init__(self, data):
        self.data = data

    def getSigma(self):
        return self.data["Sigma"]
    
    def getStates(self):
        return self.data["States"]
    
    def returnStart(self):
        return self.data["Start"]
    
    def returnFinish(self):
        return self.data["Finish"]