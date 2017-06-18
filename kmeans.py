import os
import pandas as pd
import sys
import math


a=os.path.dirname(__file__)
rel_path = sys.argv[1]
abs_file_path = os.path.join(a, rel_path)
with open(abs_file_path) as textFile:
    matrix1 = [line.split() for line in textFile]


a=len(matrix1)
matrix2=[]
k=int(sys.argv[2])
matrix2=matrix1[0:k] 
it=0   
nc=[]  

while(it<1000):
    nc=[x[:] for x in matrix2]
    clusterIndex = [[] for i in range(k)] 
    for a in range(len(matrix1)):
               
        cc=0
        dist=sys.maxsize
        for i in range(len(nc)):
            z=zip(matrix1[a],nc[i])   
            d=0.0
            for member in z:
                
                d += (float(member[1]) - float(member[0])) ** 2
            d=math.sqrt(d)   
            #print(d)
            if d<dist:
                dist=d
                cc=i
                clusterIndex[i].append(a)
                for y in range(len(clusterIndex)):
                    if a in clusterIndex[y] and y!=i:
                        clusterIndex[y].remove(a)
        for i in range(len(nc[cc])):
            
            l=clusterIndex[cc]
            #print(l)
            num=len(l)
            sum1=0
            for y in l:
                sum1+=float(matrix1[y][i])
            if num > 0:
                nc[cc][i]=sum1/num
                
            
        
        
    #print(nc)
    #print(clusterIndex)
    nc=[[str(y) for y in x] for x in nc]
    matrix2=[[str(y) for y in x] for x in matrix2]
    if nc==matrix2:
        print(nc)
        break;
    it=it+1
    if(it==1000):
        print(nc)
        break;
    matrix2=nc 
        
    

a=os.path.dirname(__file__)
rel_path = "clusters.txt"
abs_file_path = os.path.join(a, rel_path)
with open(abs_file_path,"w") as t:
    t.write(str(nc))
                    
        
    
    
        
    
