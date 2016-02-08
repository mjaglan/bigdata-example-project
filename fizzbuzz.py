# -*- coding: utf-8 -*-
'''
Write a python program called fizzbuzz.py that accepts an integer n from the command line. Pass this integer to a
function called fizzbuzz. The fizzbuzz function should then iterate from 1 to n. If the ith number is a multiple of
two, print “fizz”, if a multiple of three print “buzz”, if a multiple of both print “fizzbuzz”, else print the value.
'''

import sys

def fizzbuzz(N):
    for i in range(1,N+1,1):
        if(i%6==0):
            localVal = "fizzbuzz"
        elif(i%2==0):
            localVal = "fizz"
        elif(i%3==0):
            localVal = "buzz"
        else:
            localVal = i
        yield localVal


def stub():
    try:
        N = int(sys.argv[1])
        for val in fizzbuzz(N):
            print val,
    except:
        print "%s method requires a Natural Number as as argument!", sys.argv[0]
        exit(-1)


if __name__ == '__main__':
    stub()
