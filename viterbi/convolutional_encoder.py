import numpy as np
from numpy  import log as ln
import random as rd

def main():
    m1 = "01100000"
    m2 = "10110001"
    m3 = "01111101"
    m4 = "01100010"
    c1 = encoder(m1)
    c2 = encoder(m2)
    c3 = encoder(m3)
    c4 = encoder(m4)
    print(m1,"=>",c1)
    print(m2,"=>",c2)
    print(m3,"=>",c3)
    print(m4,"=>",c4)
    
def encoder(bits):
    reg = ['0','0','0'] # 3 bits shift register
    output = ""
    for i in range(len(bits)):
        reg[2] = reg[1]
        reg[1] = reg[0]
        reg[0] = bits[i]
        out1 = xor(xor(reg[0],reg[1]),reg[2])
        out2 = xor(reg[0],reg[2])
        if i == len(bits)-1:
            output += (out1 + out2)
        else: output += (out1 + out2 + " ")
    return output

if __name__ =="__main__":
    main()