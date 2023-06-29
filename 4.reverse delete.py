def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j][2]<x[2]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1


def Quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        Quicksort(arr,p,q-1)
        Quicksort(arr,q+1,r)


from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.V=v
        self.graph=defaultdict(list)
        self.adj=[]
    def addEdge(self,u,v,w):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.adj.append([u,v,w])

    def removeedge(self,u,v):
        self.graph[u].remove(v)
        self.graph[v].remove(u)

    def dfs(self,u,vis):
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)

    def connected(self):
        vis=[False for i in range(self.V)]

        self.dfs(0,vis)

        for i in range(self.V):
            if vis[i]==False:
                return False

        return True


    def reversedelete(self):

        Quicksort(self.adj,0,len(self.adj)-1)

        res=[]

        wt=0

        for i in range(len(self.adj)-1,-1,-1):
            u=self.adj[i][0]
            v=self.adj[i][1]
            w=self.adj[i][2]

            self.removeedge(u,v)

            if self.connected()==False:

                self.addEdge(u,v,w)

                res.append([u,v])
                wt+=w

        for i in range(len(res)):
            print(res[i])

        print('weight is ',wt)


V = 9
g = Graph(V)

# making above shown graph
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

g.reversedelete()








