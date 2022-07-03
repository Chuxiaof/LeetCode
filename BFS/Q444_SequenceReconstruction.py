class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = self.build_graph(sequences)
        topo_sort = self.topo_sort(graph)
        return topo_sort == nums

    def build_graph(self, sequences):
        graph = {}
        for seq in sequences:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in sequences:
            for i in range(1, len(seq)):
                graph[seq[i-1]].add(seq[i])

        return graph

    def in_degree(self, graph):
        in_degree = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbour in graph[node]:
                in_degree[neighbour] += 1

        return in_degree

    def topo_sort(self, graph):
        in_degree = self.in_degree(graph)
        queue = collections.deque()
        topo_sort = []

        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            if len(queue) > 1:
                return None
            node = queue.popleft()
            topo_sort.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_sort) == len(graph):
            return topo_sort

        return None
