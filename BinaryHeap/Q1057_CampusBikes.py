class Solution:
    # Approach 1: Sort by array
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

    # Approach 2: Bucket Sort
    # Total: O(n*m+k), where k <= 1998

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """ Remember
            ---------
            when we have input distributed over a known short range, 
            we can use bucket sort.

            In this problem, we have the range is (0, 1998].

            Algorithm
            ----------
            1. Generate all the (worker, bike) pairs. For each pair, find the Manhattan distance, distance. 
            2. Add this pair to the list disToPairs corresponding to the index distance.
            3. Among all the pairs generated, store the minimum distance in the variable minDis.
            4.Initialize currDis to minDis. Until all the workers have been assigned a bike, do the following:
                - Iterate over the pairs with distance currDis
                - If the worker and bike are available, assign the bike to the worker in the list workerStatus and mark the bike unavailable in bikeStatus. 
                Increment the value of pairCount which is the value of worker-bike pairs that have been made.
                - Once all the pairs with the current distance have been traversed, increment the value of currDis.
            5. Return workerStatus.

        """

        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])

        min_dist = float('inf')
        dist_to_pairs = collections.defaultdict(list)

        for worker, worker_loc in enumerate(workers):
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                dist_to_pairs[distance].append((worker, bike))
                min_dist = min(min_dist, distance)

        curr_dist = min_dist
        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
        pair_count = 0

        while pair_count < len(workers):
            for worker, bike in dist_to_pairs[curr_dist]:
                if worker_status[worker] == -1 and not bike_status[bike]:
                    bike_status[bike] = True
                    worker_status[worker] = bike
                    pair_count += 1
            curr_dist += 1

        return worker_status

    # Approach 3: Min Heap
    # Total: O(n*mlog(m))

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])

        worker_to_bike_list = []
        pq = []

        for worker, worker_loc in enumerate(workers):
            curr_worker_pairs = []
            for bike, bike_loc in enumerate(bikes):
                distance = find_distance(worker_loc, bike_loc)
                curr_worker_pairs.append((distance, worker, bike))

            curr_worker_pairs.sort(reverse=True)  # O(mlogm)
            heapq.heappush(pq, curr_worker_pairs.pop())
            worker_to_bike_list.append(curr_worker_pairs)

        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)

        while pq:
            distance, worker, bike = heapq.heappop(pq)
            if not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
            else:
                next_closest_bike = worker_to_bike_list[worker].pop()
                heapq.heappush(pq, next_closest_bike)

        return worker_status
