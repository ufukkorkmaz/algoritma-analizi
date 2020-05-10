import numpy as np
from numpy  import log as ln
import random as rd

def main():
    message = ("10","10","11","11","01","01") # karşıdan gelen kodlanmış mesaj
    init_p = {'a':0,'b':100, 'c':100,'d':100} # ilk hamming uzunlukları
    fsm = {  # Finite State Machine - Kodlayıcının durum makinesi
    'a': {'b1': {'out':"11", 'prev': 'b', 'in_b':0},
          'b2': {'out':"00", 'prev': 'a', 'in_b':0}},
    'b': {'b1': {'out':"01", 'prev': 'd', 'in_b':0},
          'b2': {'out':"10", 'prev': 'c', 'in_b':0}},
    'c': {'b1': {'out':"11", 'prev': 'a', 'in_b':1},
          'b2': {'out':"00", 'prev': 'b', 'in_b':1}},
    'd': {'b1': {'out':"10", 'prev': 'd', 'in_b':1},
          'b2': {'out':"01", 'prev': 'c', 'in_b':1}},
}
    print("encoded_message = ",list(message))
    dec = viterbi_decoder(message,init_p,fsm)
    print("decoded_message = ",dec)

def viterbi_decoder(data,init_p,fsm):
    V=[{}]
    for state in fsm:
        V[0][state] = {"metric":init_p[state]}
    for t in range(1,len(data)+1):
        V.append({})
        for state in fsm:
            prev = fsm[state]['b1']['prev']
            fbit_m = V[(t-1)][prev]['metric'] + hamming(fsm[state]['b1']['out'],data[t-1])
            prev = fsm[state]['b2']['prev']
            sbit_m = V[(t-1)][prev]['metric'] + hamming(fsm[state]['b2']['out'],data[t-1])
            if fbit_m > sbit_m:
                V[t][state] = {"metric":sbit_m, "branch":"b2"}
            else: V[t][state] = {"metric":fbit_m, "branch":"b1"}

    # print trellis nodes metric:
    """ 
    for state in fsm:
        for t in range(0,len(V)):
            print("%4d" % V[t][state]["metric"],end="")
        print()
    print()
    """
    min_metric = min(V[t][state]["metric"] for state in fsm)
    best_path = []
    # traceback the path on smaller metric on last trellis column
    for state in fsm:
        if V[len(data)-1][state]["metric"] == min_metric:
            init_state = state
            for t in range(len(data),0,-1):
                branch = V[t][init_state]['branch']
                init_state = fsm[init_state][branch]['prev']
                best_path.append(fsm[init_state][branch]['in_b'])
    return best_path

if __name__ =="__main__":
    main()