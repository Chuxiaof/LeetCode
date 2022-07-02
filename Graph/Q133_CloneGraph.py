"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodes = self.find_all_nodes(node)
        mappings = self.clone_all_nodes(node, nodes)
        self.clone_all_edges(nodes, mappings)
        
        return mappings[node]
    
        
    def find_all_nodes(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return list(visited)
    
    def clone_all_nodes(self, node, nodes):
        mappings = {}
        for node in nodes:
            mappings[node] = Node(node.val, [])
            
        return mappings
    
    def clone_all_edges(self, nodes, mappings): 
        for node in nodes:
            new_node = mappings[node]
            for neighbor in node.neighbors:
                new_neighbor = mappings[neighbor]
                new_node.neighbors.append(new_neighbor)


    # simple BFS template for finding all nodes 
    queue = collections.deque([node])
    distances = {node : 0}
    while queue:
        curr_node = queue.popleft()
        for neighbor in curr_node.neighbors:
            if neighbor in distances:
                continue
            queue.append(neighbor)
            distances[neighbor] = distances[curr_node] + 1
            



                