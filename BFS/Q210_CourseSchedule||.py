class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []

        in_order = [0] * numCourses

        graph = [[] for _ in range(numCourses)]
        for in_course, out_course in prerequisites:
            in_order[in_course] += 1
            graph[out_course].append(in_course)

        queue = collections.deque()
        for i in range(numCourses):
            if in_order[i] == 0:
                queue.append(i)

        num_choose = 0
        topo_order = []

        while queue:
            curr_course = queue.popleft()
            num_choose += 1
            topo_order.append(curr_course)
            for next_course in graph[curr_course]:
                in_order[next_course] -= 1
                if in_order[next_course] == 0:
                    queue.append(next_course)

        return topo_order if num_choose == numCourses else []
