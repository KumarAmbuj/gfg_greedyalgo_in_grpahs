class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=[[0 for i in range(self.V)] for j in range(self.V)]

    def findmin(self,vis,dis):

        min=99
        minindex=-2

        for i in range(self.V):
            if dis[i]<min and vis[i]==False:
                min=dis[i]
                minindex=i

        return minindex

    def printprims(self,parent,dis):

        for i in range(self.V):
            print(parent[i],'..',i,':',dis[i])


    def primsalgo(self,src):

        vis=[False for i in range(self.V)]
        dis=[999 for i in range(self.V)]
        parent=[-1 for j in range(self.V)]

        dis[src]=0

        for c in range(self.V):

            u=self.findmin(vis,dis)

            vis[u]=True

            for v in range(self.V):

                if self.graph[u][v]>0 and vis[v]==False and dis[v]>self.graph[u][v]:
                    dis[v]=self.graph[u][v]

                    parent[v]=u

        self.printprims(parent,dis)
        

g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primsalgo(0);