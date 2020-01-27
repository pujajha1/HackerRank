#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?h_r=next-challenge&h_v=legacy
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_holder=[]
    max_holder=[]
    counter_min=0
    counter_max=0
    min_holder.append(scores[0])
    max_holder.append(scores[0])
    for i in scores:
        m=min_holder.pop()
        mx=max_holder.pop()
        if i>=m:
            #print("m")
            #print(m)
            min_holder.append(m)
        else:
            #print("i")
            #print(i)
            min_holder.append(i)
            counter_min+=1
            ############################
        if i<=mx:
            #print("m")
            #print(m)
            max_holder.append(mx)
        else:
            #print("i")
            #print(i)
            max_holder.append(i)
            counter_max+=1
        
        
    return (counter_max,counter_min)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
