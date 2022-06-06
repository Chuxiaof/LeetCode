class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s, f, ans = 0, 0, 0
        maxx = collections.deque()
        minn = collections.deque()

        for num in nums:
            while maxx and maxx[-1] < num:
                maxx.pop()
            while minn and minn[-1] > num:
                minn.pop()

            maxx.append(num)
            minn.append(num)

            while (maxx[0] - minn[0]) > limit:
                if nums[s] == maxx[0]:
                    maxx.popleft()
                if nums[s] == minn[0]:
                    minn.popleft()
                s += 1

            ans = max(f-s+1, ans)
            f += 1

        return ans
