import random

N = 100

edges = []


clusters1 = [0,10,20,30,40,50,60,70,80,90,N]
clusters1 = [[clusters1[i],clusters1[i+1]] for i in range(len(clusters1)-1)] 

p1 = 0.8
q1 = 0.05

clusters2 = {0:[1,2],3:[4,5],6:[1,7,8]}

p2 = 0.1


def getcluster(i,clusters):
    for c,(cL,cR) in enumerate(clusters):
        if i>=cL and i<cR:
            return c
    return None

for i in range(N):
    c1 = getcluster(i,clusters1)    
    for j in range(N):
        c2 = getcluster(j,clusters1)
        if i != j: 
            if c2 == c1:
                p = p1
            elif c1 in clusters2.keys():
                if c2 in clusters2[c1]:
                    p = p2
            elif c2 in clusters2.keys():
                if c1 in clusters2[c2]:
                    p = p2
            else:
                p = q1 
            if random.random() < p:
                if [i,j] not in edges and [j,i] not in edges:
                    edges.append([i,j])
                    print '%d,%d' % (i+1,j+1)
