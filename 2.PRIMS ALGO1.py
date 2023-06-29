class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=[[0 for i in range(self.V)] for j in range(self.V)]

    def findmin(self,key,mstset):

        min=999

        minindex=-1

        for i in range(self.V):
            if key[i]<min and mstset[i]==False:
                min=key[i]
                minindex=i

        return minindex


    def printprims(self,key,parent):

        for i in range(1,self.V):
            print(parent[i],'...',i,':',key[i])


    def primsalgo(self):

        key=[999 for i in range(self.V)]

        parent=[-1]*self.V

        mstset=[False for i in range(self.V)]


        key[0]=0

        for cout in range(self.V):

            u=self.findmin(key,mstset)

            mstset[u]=True

            for v in range(self.V):

                if self.graph[u][v]>0 and mstset[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u


        self.printprims(key,parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

g.primsalgo();



