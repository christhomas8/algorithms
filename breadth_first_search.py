#Initialize empty graph of edges
G = []

#function for adjacency edges (neighbors)
def adj(node):
    v = []
    for i in range(len(G)):
        if G[i][0] == node:
            v.append(G[i][1])
    return v
    

#Breadth First Search Function (G(graph), s(source node))
def BFS(G,s):

    #let Q be the queue and store source node (enqueue( s ))
    Q = []
    Q.append(s) 
    
    #let V be visited nodes
    V = []

    #while ( Q is not empty)
    while Q:
        #children of current node
        child = adj(Q[0])

        #add children to Q
        for i in range(len(child)):
            if (child[i] not in Q) and (child[i] not in V):
                Q.append(child[i])
            print("Queue: ",Q)

        #remove FIFO of queue
        V.append(Q[0])
        Q.pop(0)
    
    print("Vertices Visited: ",V)

#add edge [x,y];future: z-is directed or undirected
def addE(x,y):
    G.append([x,y])
    #G.append([y,x])

######################################
#Construct Main Graph
addE(1,2)
addE(1,3)
addE(1,8)
addE(8,9)
addE(9,10)
addE(8,10)
addE(2,4)
addE(2,5)
addE(2,6)
addE(3,6)
addE(4,5)
addE(8,7)

#Breadth First Search Called (starting at node 1)
BFS(G,1)
