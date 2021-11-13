print("Welcome, this is the code for bellman ford algorithm !!!")
INFINITY=9999999999999

def bellmanFord(MAT,len1):
    for i in range(len1-1):
        for u in range(len1):
            for v in range(len1):
                if dist[u]+MAT[u][v]<dist[v] :
                    dist[v]=dist[u]+MAT[u][v]
                    parent[v]=u;
    print("Distance Vector {}".format(dist))
    print("Parent Vector {} ".format(parent))

                

MAT=[
[0,3,INFINITY,7],
[8,0,2,INFINITY],
[5,INFINITY,0,1],
[2,INFINITY,INFINITY,0]
]
len1 = len(MAT)
dist = [(INFINITY if i > 0 else 0) for i in range(len1)]
parent=[None for i in range(len1)]
bellmanFord(MAT,len1)