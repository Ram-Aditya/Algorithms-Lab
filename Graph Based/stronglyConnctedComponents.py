from collections import defaultdict

class Graph:
    def __init__(self,nverts):
        self.adj=defaultdict(list)
#Vars for DFS
        self.visited=[0]*nverts
        self.st=[0]*nverts
        self.en=[0]*nverts
        self.time=0
        self.enq=[]
#End of Vars for DFS
        self.nsem=0
        self.nverts=nverts
        self.sverts=[]
        self.ninc=[0]*nverts
        self.act=[1]*nverts
        self.gelem=nverts

    def addEdge(self,e1,e2):
        self.adj[e1].append(e2)

    def DFS(self,source):
        self.time=self.time+1
        self.visited[source]=1
        self.st[source]=self.time
        for i in self.adj[source] :
            if(self.visited[i]==0) :
                self.DFS(i)
        self.time=self.time+1
        l=[self.time,source]
        self.enq.append(l)
        self.en[source]=self.time

    def revGraph(self):
        tadj=defaultdict(list)
        for i in range(self.nverts):
            for j in self.adj[i]:
                tadj[j].append(i)
        return tadj

    def findSource(self):
        radj=self.revGraph()
        for i in range(self.nverts):
            self.ninc[i]=len(radj[i])
            if(self.ninc[i]==0):
                self.sverts.append(i)
    def topSort(self):
        if(self.gelem>0):
            self.gelem=self.gelem-len(self.sverts)
            print(self.sverts,end=' ')
            self.nsem=self.nsem+1
            self.sverts=[]
            for j in temp:
                for i in self.adj[j]:
                    self.ninc[i]=self.ninc[i]-1
                    if(self.ninc[i]==0):
                        self.sverts.append(i)
            self.topSort()

    def DFS1(self,source,visited):
        visited[source]=1
        print(source,end=' ')
        self.act[source]=0
        for i in self.adj[source]:
            if i not in visited and self.act[i]==1:
                self.DFS1(i,visited)

    def scc(self,RG):

        if(len(RG.enq)>0):
            source=None
            while(len(RG.enq)!=0):
                t=RG.enq.pop()
                if(self.act[t[1]]==1):
                    source=t[1]
                    break
            visited={}
            if(source is not None):
                self.DFS1(source,visited)
            print(' ')
            self.scc(RG)

n=int(input("No. of Vertices "))
e=int(input("No. of Edges "))
G=Graph(n)
RG=Graph(n)
for i in range(e):
    l=input().split()
    G.addEdge(int(l[0]),int(l[1]))
    RG.addEdge(int(l[1]),int(l[0]))
for i in range(n):
    if(RG.visited[i]==0):
        RG.DFS(i)
G.scc(RG)
