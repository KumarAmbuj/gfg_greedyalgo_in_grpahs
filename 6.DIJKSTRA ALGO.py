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

    def printdij(self,dis,parent,src):

        for i in range(self.V):
            path=[]
            if i==src:
                continue

            path.append(i)

            v=i
            while(v!=src):
                v=parent[v]
                path.append(v)
            path.reverse()

            print('distance from src',src,' to ',i,'is ',dis[i],'and path is ',path)






    def dijsalgo(self,src):

        dis=[999 for i in range(self.V)]
        vis=[False for i in range(self.V)]
        parent=[-1 for j in range(self.V)]

        dis[src]=0

        for c in range(self.V):

            u=self.findmin(vis,dis)

            vis[u]=True

            for v in range(self.V):
                if self.graph[u][v]>0 and vis[v]==False and dis[v]>dis[u]+self.graph[u][v]:
                    dis[v]=dis[u]+self.graph[u][v]
                    parent[v]=u

        self.printdij(dis,parent,src)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijsalgo(1)