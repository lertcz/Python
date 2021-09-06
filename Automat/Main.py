from Process.IO import getData
from Process.Parse import Parse
from Process.Simulation import Simulation
#Σ

#init 
data = getData("Automat_Epsilon_Deterministic.json")
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
output = simulation.simulate(Input, data)

#output
print(output)