#!/usr/bin/env python
# coding: utf-8

def brackets_seq(s):
    stack = []
    pairs = {'}':'{', ']':'[', ')':'('}
    flag = 1
        
    for c in s:
        if c in '{[(':
            stack.append(c)
        elif c in '}])':
            if (len(stack) == 0):
                flag = 0
                break
            else:
                result = stack.pop() 
                if (result != pairs[c]):
                    flag = 0
                    break
                    
    if ((len(stack) == 0) and (flag == 1)):
        print("YES")
    else:
        print("NO")

