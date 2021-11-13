print("Welcome, this is the code for bellman ford algorithm !!!")

INFINITY=9999999999999
class Graphs :
        def __init__(self):
            self.__MAT=[]
            self.__len1=-1

        def __initialize(self,GRAPH,Source):
            self.__MAT = GRAPH
            self.__len1 = len(GRAPH)
            self.__dist = [(INFINITY if not i  == Source else 0) for i in range(self.__len1)]
            self.__parent = [None for i in range(self.__len1)]



        def __bellmanFord(self):
            for i in range(self.__len1-1):
                for u in range(self.__len1):
                    for v in range(self.__len1):
                        if self.__dist[u]+self.__MAT[u][v]<self.__dist[v] :
                            self.__dist[v]=self.__dist[u]+self.__MAT[u][v]
                            self.__parent[v]=u
            str1=str(self.__dist)
            for u in range(self.__len1):
                for v in range(self.__len1):
                    if self.__dist[u] + self.__MAT[u][v] < self.__dist[v]:
                        self.__dist[v] = self.__dist[u] + self.__MAT[u][v]
                        self.__parent[v] = u

            return str1==str(self.__dist)

        def __dijkshtra(self):

            # Under Construction
            pass

        def __getPath(self,u,v):
            self.__path=str(v)
            temp=v
            while not temp == u :
                temp=self.__parent[temp]
                self.__path=str(temp)+" >> "+self.__path
            return self.__path

        def printPath(self,GRAPH,Source,Destination,algo):
            self.__initialize(GRAPH,Source)
            if Source>=self.__len1 or Destination >=self.__len1 :
                print("Source or Destination mentioned does not exists , Terminating ...");
            else :
                if algo=='b' :
                    if self.__bellmanFord() :
                        print(self.__getPath(Source,Destination));
                    else :
                        print("path cannot be found since graph given by you has negative weight cycle !!");
                elif algo=='d' :
                    self.__dijkshtra()
                    print(self.__getPath(Source, Destination));


MAT=[
[0,3,INFINITY,7],
[8,0,2,INFINITY],
[5,INFINITY,0,1],
[2,INFINITY,INFINITY,0]
]

MAT3=[
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

MAT1=\
[[0,-9,INFINITY],[INFINITY,0,2],[3,INFINITY,0]]

gr=Graphs()

#gr.printPath(MAT,0,3,'b') # Graph with no negative weight cycle

#gr.printPath(MAT1,0,2,'b') # Graph with negative weight cycle


gr.printPath(MAT3,1,7,'b')

#Its responsibility of user
# to make sure that graph has no -ve weights
# if he/she uses DIJKSHTRA's algorithm
#gr.printPath(MAT1, 3, 2, 'd') #dijkshtra's Algorithm more efficient than bellmanford