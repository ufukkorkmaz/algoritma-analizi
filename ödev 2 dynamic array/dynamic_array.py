#!/usr/bin/env python

"""Dinamik Array ile Amortization (amortized cost analizi )"""

import ctypes
import sys
import random as rd

__author__ = "Ufuk KORKMAZ"
__copyright__ = "Copyright 2020"
__license__ = "GPLv3"
__version__ = "1.0.1"
__email__ = "190401109@ogr.comu.edu.tr"
__status__ = "Development"


class DArray(object):
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._array = self.__create_low_level_array(self._capacity)
    
    def __len__(self):return self._n
    
    def __getitem__(self,i):
        if 0 <= i < self._n: return self._array[i]
        else: raise IndexError("index out of range")
        
    def __resize_array(self,capacity):                             # private method
        new_array = self.__create_low_level_array(capacity)
        for i in range(self._n): new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = capacity
    
    def __create_low_level_array(self,capacity):                   # private method, C array tipinde dizi oluşturur
        py_obj_array = capacity * ctypes.py_object
        return py_obj_array()
    
    def append(self,obj):
        if self._n == self._capacity: self.__resize_array(2*self._capacity)    # array kapasitesi iki katını alır 
        self._array[self._n] = obj
        self._n += 1
        print("Eleman eklendi!")
    
    def remove(self):                                               # array boş değilse ancak eleman silinecek 
        if self._n > 0:
            self._array[self._n] = None
            self._n -= 1
            print("Son eleman silindi!")   

def main(argv):
    darray = DArray()
    
    darray.append(rd.randint(0,100))
    darray.append(rd.randint(0,100))
    darray.append(rd.randint(0,100))
    darray.append(rd.randint(0,100))
    darray.append(rd.randint(0,100))
    
    print("Dizi son hali:")
    for i in darray: print(i)
    
    darray.remove()
    darray.remove()
    
    print("Dizi son hali:")
    for i in darray: print(i)
        

if __name__ == "__main__":
    main(sys.argv[1:])
