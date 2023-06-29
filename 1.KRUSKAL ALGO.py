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

class Graph():
    def __init__(self,v):
        self.v=v
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i]==-1:
            return i
        else:
            return self.find(parent,parent[i])


    def Kruskal(self):

        Quicksort(self.graph,0,len(self.graph)-1)

        parent=[-1]* self.v

        e=0

        i=0

        res=[]

        while(e<self.v-1):

            u,v,w=self.graph[i]
            i+=1

            x=self.find(parent,u)
            y=self.find(parent,v)

            if x!=y:

                e+=1

                parent[v]=u

                res.append([u,v,w])

        for u,v,w in res:
            print(u,'...',v,':',w)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.Kruskal()



