#Multiple Source Shortest Distance Algorithm
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
]
'''

dist=[
[0,3,INFINITY,7],
[8,0,2,INFINITY],
[5,INFINITY,0,1],
[2,INFINITY,INFINITY,0]
]
sources = [[],[],[],[]]
'''
dist=[
[0,3,INFINITY,5],
[2,0,INFINITY,4],
[INFINITY,1,0,INFINITY],
[INFINITY,INFINITY,2,0]
]
'''

for i in range(len(dist)):
    for u in range(len(dist)) :
        for v in range(len(dist)):
            if dist[u][v]> dist[u][i]+dist[i][v] :
                dist[u][v]=dist[u][i]+dist[i][v];
    


print(dist);
    
        








