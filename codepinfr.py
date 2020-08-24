import random

def generatePIN():
    
    PIN = ""
    
    for i in range(4):
        
        PIN = PIN + str(random.randint(0,9))
    return(f"PIN à 4 chiffres:{PIN}")

print(generatePIN())