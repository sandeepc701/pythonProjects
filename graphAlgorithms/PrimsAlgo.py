# Minimum Spanning Tree Algorithm

INFINITY=99999999999999;
'''dist=[
[0,4,INFINITY,INFINITY,16,INFINITY,INFINITY,INFINITY,5,18],
[4,0,7,9,INFINITY,INFINITY,INFINITY,INFINITY,10,INFINITY],
[INFINITY,7,0,8,INFINITY,INFINITY,INFINITY,INFINITY,INFINITY,INFINITY],
[INFINITY,9,8,0,10,INFINITY,INFINITY,14,INFINITY,INFINITY],
[16,INFINITY,INFINITY,10,0,21,INFINITY,INFINITY,INFINITY,INFINITY],
[INFINITY,INFINITY,INFINITY,INFINITY,21,0,24,INFINITY,INFINITY,INFINITY],
[INFINITY,INFINITY,INFINITY,INFINITY,INFINITY,24,0,20,18,10],
[INFINITY,INFINITY,INFINITY,14,INFINITY,INFINITY,20,0,11,16],
[5,10,INFINITY,INFINITY,INFINITY,INFINITY,18,11,0,9],
[18,INFINITY,INFINITY,INFINITY,INFINITY,INFINITY,10,16,9,0]
]'''

dist=[
[0,10,60,20],
[10,0,40,50],
[60,40,0,30],
[20,50,30,0]
]

Cost=[INFINITY]*len(dist);
visited=[False]*len(dist);
parent=[None]*len(dist);

source=0;

Cost[source]=0;
parent[source]=0;

def getMin():
    n=INFINITY
    ind=-1
    for i in range(len(Cost)) :
        if Cost[i]<n and not(visited[i]) :
            n=Cost[i];
            ind=i;
    visited[ind]=True;
    return ind;
    
def relax(ind):
    for i in range(len(Cost)) :
        if Cost[i]>(dist[ind][i]) and not(visited[i]) :
            Cost[i]=dist[ind][i];
            parent[i]=ind;
    
def scan():
    for val in visited:
        if not(val):
           return not(val);
    return False;
             
             
while(scan()):
    val=getMin()
    relax(val)
print(Cost,end='\n')
print(parent)




#C:\Users\schau2\AppData\Local\Programs\Python\Python38-32\python.exe  "c:\Users\schau2\Desktop\PrimAlgo.py"

