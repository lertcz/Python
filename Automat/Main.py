from Process.IO import getData
from Process.Parse import Parse
from Process.Simulation import Simulation
#Σ

#init 
data = getData("Automat.json") #"Automat_Epsilon.json")
parse = Parse(data)
simulation = Simulation(parse.returnStart(), parse.returnFinish(), parse.getSigma())

#get sigma and states
sigma = parse.getSigma()
states = parse.getStates()

#print sigma, states, and get input
print("Σ:", sigma)
print(states)
Input = input("Input: ")

#simulation
output = simulation.simulate(states, Input, data)

#output
print(output)

#file:///C:/Users/Pavel/Desktop/IFJ/Ifj04-anim-cz.pdf