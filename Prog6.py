#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:49:31 2021

@author: mohanthapa
"""


import string

from collections import defaultdict


def open_file():
    while True:
        try:
            
            fv = input("Enter a  filename: ")
            fp = open(fv,'r')
            break
        except:
            pass
            
        print ('File doesn\'t exist')
    return fp

def read_data(fp):
    lst = []
    data_dic = defaultdict(set)
    count = 0
    
    while True:
       
        count += 1
        data = fp.readline()
       

        if len(data) == 0:
            break
        
        data = data.lower()
        
        data = data.translate( string.punctuation)
       
        lst = data.split(" ")
        
        
        for word in lst:
            if not len(word)<2: #and  w.isalpha():
             data_dic[word].add(count)
            
    return dict(data_dic)
    

def find_cooccurrence(D, inp_str):
    lst = inp_str.split(" ")
    inp_set = set()
    print("The occurence for: ",inp_str )
    print ("Lines: ")
    for i in lst:
        if i not in D:
            
            print ("No co-occurrence")
            return
        else:
            
            if len(inp_set) == 0:
                inp_set.update(D[i])
           
            else:
                inp_set.intersection_update(D[i])
   
    print (", ".join(str(j) for j in inp_set))

def main():
    fp = open_file()
    dic = read_data(fp)
    inp = ""
   
    while True:
        inp = input("Input words separated by white space(q to exit): ")
        if inp=='q' or inp=='Q':
            break
        find_cooccurrence(dic, inp)

if __name__ == "__main__":
    main()

    