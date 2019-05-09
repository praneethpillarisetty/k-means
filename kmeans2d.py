import statistics as s
import math as m
a=[]
print("enter c ordinate")
p=int(input())
for i in range(p):
    x=float(input())
    y=float(input())
    a+=[[x,y]]

n=int(input("enter no of cluseters"))
kold=[]
knew=[]
def my_comp(point1):
    return point1[0]*point1[0] + point1[1]*point1[1]
a.sort(key=my_comp)
print(a)
for i in range(n):
    k=a[i*len(a)//n:(i+1)*len(a)//n]
    l=len(k)
    x=0
    y=0
    for j in range(l):
        x+=int(k[j][0])
        y+=int(k[j][1])
    kold+=[(x/l,y/l)]
knew = kold
non=[0*2]*n
k1=[0]*n
k2=[0]*n
for i in range(len(a)):
        dist=[]
        for j in range(n):
               dist+=[m.sqrt( (knew[j][0]-a[i][0])**2 + (knew[j][1]-a[i][1])**2 )]
        print(a[i],"is in cluseter:",dist.index(min(dist))+1)
        k1[dist.index(min(dist))]+=a[i][0]
        k2[dist.index(min(dist))]+=a[i][1]
        non[dist.index(min(dist))]+=1
for i in range(n):
    print(k1[i]/non[i],k2[i]/non[i],"  are the centroids")

