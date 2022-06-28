class TwoSum:

    def __init__(self):
        self.nums = []
        self.isSorted = False
        
    # time: O(1), space:O(n)
    def add(self, number: int) -> None:
        # method 1
        # time: O(nlog(n)), space:O(1)
        self.nums.append(number)
        self.isSorted = False

        # method 2
        # time: O(n), space:O(1)
        self.nums.append(number)
        idx = len(self.nums) - 1
        while(idx > 0 and self.nums[idx] < self.nums[idx - 1]):
            self.nums[idx], self.nums[idx - 1] = self.nums[idx - 1], self.nums[idx]
            idx -= 1

        

    def find(self, value: int) -> bool:
        # method 1: Two Pointers
        # time: O(nlog(n)), space:O(1)
        if not self.isSorted:
            self.nums.sort()
            self.isSorted = True
            
        left, right = 0, len(self.nums) - 1
        while(left < right):
            if self.nums[left] + self.nums[right] < value:
                left += 1
            elif self.nums[left] + self.nums[right] > value:
                right -= 1
            else:
                return True
        return False

        # method 2: HashMap
        # time: O(n), space:O(n)
        nums_dict = {}
        for i in range(len(self.nums)):
            if value - self.nums[i] in nums_dict.keys():
                return True
            
            nums_dict[self.nums[i]] = nums_dict.get(self.nums[i], 0) + 1
            
        return False
            