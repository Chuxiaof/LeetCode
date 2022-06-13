class Solution:
    # approach1: min heap
    # Total: O(nlog(l)), l is the number of ladders
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        diff, ladder_used = [], []

        for i in range(len(heights)-1):
            diff.append(heights[i+1] - heights[i])
            if diff[i] <= 0:
                continue
            if ladders:
                ladders -= 1
                heapq.heappush(ladder_used, diff[i])

            else:
                if not ladder_used or (ladder_used and ladder_used[0] > diff[i]):
                    bricks -= diff[i]

                else:
                    bricks -= heapq.heappop(ladder_used)
                    heapq.heappush(ladder_used, diff[i])

                if bricks < 0:
                    return i

        return len(heights) - 1
