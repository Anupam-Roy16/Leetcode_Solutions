class Solution:
    # first point is coonected then run krushkal . used disjoiont set with union by size
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def find_ul_par(node ):
            if node == parent[node]:
                return node
            else:
                parent[node] = find_ul_par(parent[node])
                return parent[node]


        def union_by_size(ul_par1,ul_par2):
            if size[ul_par1] > size[ul_par2]:
                parent[ul_par2] = ul_par1
                size[ul_par1] += size[ul_par2]
            else:
                parent[ul_par1] = ul_par2
                size[ul_par2] += size[ul_par1]

        def union_by_rank(ul_par1,ul_par2):
            if rank[ul_par1] == rank[ul_par2]:
                parent[ul_par2] = ul_par1
                rank[ul_par1] += 1
            elif rank[ul_par1] > rank[ul_par2]:
                parent[ul_par2] = ul_par1
            else:
                parent[ul_par1] = ul_par2

        def krushkal(graph):
            def function(par):
                return par[2]
            graph = sorted(graph, key=function)
            mst_cost=0
           
            for edge in graph:
                node1,node2,cost = edge
                ul_par1 = find_ul_par(node1)
                ul_par2 = find_ul_par(node2)
                if ul_par1 != ul_par2:
                    mst_cost += cost
                    
                    union_by_size(ul_par1, ul_par2)
                    #union_by_rank(ul_par1, ul_par2)
                   
            return mst_cost
        
        graph= []
        def add_edge(u, v, cost):
            graph.append([u, v, cost])
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                    add_edge(i,j,abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))

        #rank = [0]*(num_node + 1)
        size = [1]*(len(points))
        parent = []
        for i in range(len(points)):
            parent.append(i)
       
        return krushkal(graph)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        