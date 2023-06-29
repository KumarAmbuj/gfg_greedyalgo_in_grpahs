class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=[[0 for i in range(self.V)] for j in range(self.V)]

    def findmin(self,dist,mstset):
        min=9999
        minindex=-1

        for i in range(self.V):
            if dist[i]<min and mstset[i]==False:
                min=dist[i]
                minindex=i
        return minindex

    def printprims(self,parent,dist):
        for i in range(self.V):
            print(parent[i],'...',i,':',dist[i])


    def primsalgo(self,src):

        dist=[999 for i in range(self.V)]
        parent=[-1 for i in range(self.V)]
        mstset=[False for i in range(self.V)]

        dist[src]=0

        for cou in range(self.V):

            u=self.findmin(dist,mstset)
            mstset[u]=True


            for v in range(self.V):

                if self.graph[u][v]>0 and mstset[v]==False and dist[v]>self.graph[u][v]:
                    dist[v]=self.graph[u][v]
                    parent[v]=u

        self.printprims(parent,dist)

g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primsalgo(4);