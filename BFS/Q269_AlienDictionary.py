class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        topo_order = self.topo_sort(graph)

        return topo_order

    def build_graph(self, words):
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = set()

        for i in range(1, len(words)):
            word_out, word_in = words[i-1], words[i]
            for j in range(min(len(word_out), len(word_in))):
                if word_out[j] != word_in[j]:
                    graph[word_out[j]].add(word_in[j])
                    break
                if j == min(len(word_out), len(word_in)) - 1:
                    if len(word_out) > len(word_in):
                        return {}

        return graph

    def in_degree(self, graph):
        in_degree = {
            node: 0
            for node in graph
        }

        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

        return in_degree

    def topo_sort(self, graph):
        in_degree = self.in_degree(graph)
        topo_order = ""
        queue = [node for node in in_degree if in_degree[node] == 0]
        heapq.heapify(queue)

        while(queue):
            curr_node = heappop(queue)
            topo_order += curr_node
            for neighbor in graph[curr_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    heappush(queue, neighbor)

        if len(topo_order) == len(graph):
            return topo_order

        return ""
