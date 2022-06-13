class Solution:
    # Total: O(m*nlog(m*n))
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        ans, dists = [-1]*len(workers), []
        # O(m*n)
        for idx1, w in enumerate(workers):
            for idx2, b in enumerate(bikes):
                Manhattan_dist = abs(b[0]-w[0])+abs(b[1]-w[1])
                dists.append((Manhattan_dist, idx1, idx2))

        dists.sort()  # O(m*nlog(m*n))
        bike_taken = set()
        # O(m*n)
        for distance, i, j in dists:
            if ans[i] == -1 and j not in bike_taken:
                ans[i] = j
                bike_taken.add(j)

        return ans
