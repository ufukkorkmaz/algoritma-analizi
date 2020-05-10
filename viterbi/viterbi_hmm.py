import numpy as np
from numpy  import log as ln
import random as rd


def main():
    obs_space = [0,1] 
    data = np.array([0,0,1,1,0,1,0,0]) 
    states = {'a':'00','b':'01','c':'10','d':'11'} 
    prob = np.full(4,1/4)
    transition = np.array([[0.18,0.82,0,0],[0,0,0.65,0.35],[0.19,0.81,0,0],[0,0,0.32,0.68]]) # NxN Matrix
    emission = np.array([[0.76,0.24],[0.05,0.95],[0.89,0.11],[0.02,0.98]]) # NxM Matrix
    best_path, t1, t2 = viterbi(data,states,prob,transition,emission)
    print("observations  = ", data)
    print("best_path = ", best_path)
    print("The best path is the sequence of states having the most likely probability.")

def viterbi(data,states,prob,transition,emission):
    # initialization
    N = len(states) 
    T = len(data)                          # truncation length of the VA
    T1 = np.empty((N,T),dtype=np.single)   # tracking table for metrics of the survivor path 
    T2 = np.empty((N,T), dtype=np.uint8)   # tracking table for the survivor path 
    
    # initialization of tracking tables at t= 0
    T2[:,0] =  0
    T1[:,0] = prob * emission[:,data[0]]
    # updating the tracking tables for t = 1,2,...T
    for i in range(1,T):
        T1[:, i] = np.max(T1[:, i - 1] * transition.T * emission[np.newaxis, :, data[i]].T, 1)
        T2[:, i] = np.argmax(T1[:, i - 1] * transition.T, 1)
    
    # computing the survivor path
    survivor_path = np.empty(T, dtype=np.uint8)
    survivor_path[-1] = np.argmax(T1[:, T - 1])
    for i in range(T-1,0,-1):
        survivor_path[i-1] = T2[survivor_path[i],i]
    
    return survivor_path, np.around(T1,decimals=3), T2

if __name__ =="__main__":
    main()