f = open("Hello_World.bf", "r") #CodeHelloWorld
Code = f.read()
CodeLen = len(Code)

Memory = [0 for x in range(2**16)]
pointer = 0

#check if there is no syntax error
Open = Code.count("[")
Closed = Code.count("]")
if Open != Closed:
    print("Open brackets dont match Closed brackets!\ Shutting down.")
    quit()
startPos = 0
Open = 0
Closed = 0

step = 0

while step != CodeLen:
    char = Code[step]


    if(char == ">"):
        pointer = pointer + 1 if pointer < len(Memory)-1 else 0

    elif(char == "<"):
        pointer = pointer - 1 if pointer > 0 else len(Memory)-1

    elif(char == "+"):
        Memory[pointer] = Memory[pointer] + 1 if Memory[pointer] < 255 else 0

    elif(char == "-"):
        Memory[pointer] = Memory[pointer] - 1 if Memory[pointer] > 0 else 255

    elif(char == "."):
        print(chr(Memory[pointer]), end="")

    elif(char == "["):
        loopStart = step
        Open += 1

    elif(char == "]" and Closed+1 == Open):
        if Memory[pointer] != 0:
            step = loopStart
        
        else:
            Closed += 1
    
    step += 1
    #print(step, Memory)

f.close()