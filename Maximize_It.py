# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
from itertools import permutations
import sys

input_list=[]
for line in sys.stdin:
    line=line.replace("\n","").split(" ")
    line=[eval(i) for i in line]
    input_list.append(line)
    

k=input_list[0][0]
m=input_list[0][1]

solutions_list=[]

 
# initializing list of list
all_list=[]
for i in range(1,1+k):
    all_list.append(input_list[i])

 
# using itertools.product() 
# to compute all possible permutations
res = list(itertools.product(*all_list))

#Remove duplicates
res=list(dict.fromkeys(res))
 
def get_arguments(k_list):
    return (sum(i*i for i in k_list))

k_list=[]    
for i in range(k):
    k_list.append(i)
for permutation in res:
    permutation_list=[]

    for item in k_list:
        x=permutation[item]
        permutation_list.append(x)

    solution=(get_arguments(permutation_list))%m
    solutions_list.append(solution)
    
    

print(max(solutions_list))

