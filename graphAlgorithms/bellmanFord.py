print("Welcome, this is the code for bellman ford algorithm !!!")

INFINITY=9999999999999
class Graphs :
        def __init__(self):
            self.__MAT=[]
            self.__len1=-1

        def __initialize(self,GRAPH):
            self.__MAT = GRAPH
            self.__len1 = len(GRAPH)
            self.__dist = [(INFINITY if i > 0 else 0) for i in range(self.__len1)]
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

        def __getPath(self,u,v):
            self.__path=str(v)
            temp=v
            while not temp == u :
                temp=self.__parent[temp]
                self.__path=str(temp)+" >> "+self.__path
            return self.__path

        def printPath(self,GRAPH,Source,Destination,algo):
            self.__initialize(GRAPH)
            if algo=='b' :
                if self.__bellmanFord() :
                    print(self.__getPath(Source,Destination));
                else :
                    print("path cannot be found since graph given by you has negative weight cycle !!");
            else :
                pass # under construction !!!!


MAT=[
[0,3,INFINITY,7],
[8,0,2,INFINITY],
[5,INFINITY,0,1],
[2,INFINITY,INFINITY,0]
]

MAT1=\
[[0,-9,INFINITY],[INFINITY,0,2],[3,INFINITY,0]]

gr=Graphs()

gr.printPath(MAT,0,3,'b') # Graph with no negative weight cycle

gr.printPath(MAT1,0,3,'b') # Graph with negative weight cycle