class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=[[ 0 for i in range(self.V)] for j in range(self.V)]

    def findmin(self,dis,vis):
        min=999
        minindex=-2

        for i in range(self.V):
            if dis[i]<min and vis[i]==False:
                min=dis[i]
                minindex=i
        return minindex

    def printdij(self,par,dis,src):

        for i in range(self.V):
            if i==src:
                continue

            path=[]
            v=i
            path.append(v)
            while(v!=src):
                v = par[v]
                path.append(v)

            path.reverse()

            print('dist from src ',src,'to ',i,' is',dis[i],'path is ',path)


    def dijsalgo(self,src):

        dis=[999 for i in range(self.V)]
        vis=[False for i in range(self.V)]
        par=[-1 for j in range(self.V)]

        dis[src]=0

        for c in range(self.V):

            u=self.findmin(dis,vis)

            vis[u]=True

            for v in range(self.V):

                if self.graph[u][v]>0 and vis[v]==False and dis[v]>dis[u]+self.graph[u][v]:
                    dis[v]=dis[u]+self.graph[u][v]
                    par[v]=u

        self.printdij(par,dis,src)


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

g.dijsalgo(8)