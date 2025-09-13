def rotateBinary(bina,steps):

    steps=steps%len(bina) #make steps into a loop type thing so any value is accepted

    rotatedVal=bina[steps:] + bina[:-steps]
    dec=int(rotatedVal, 2)

    return dec

b="10000111100101100"

print(rotateBinary(b,4))

