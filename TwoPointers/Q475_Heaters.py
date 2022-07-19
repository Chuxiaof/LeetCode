class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    # approach 1: binary search
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        # Write your code here
        heaters.sort()
        max_radius = 0
        for house in houses:
            max_radius = max(self.find_min_radius(heaters, house), max_radius)
        
        return max_radius
    
    def find_min_radius(self, heaters, house):
        left, right = 0, len(heaters) - 1
        while(left + 1 < right):
            mid = (left + right) // 2
            if heaters[mid] <= house:
                left = mid
            else:
                right = mid

        return min(abs(house - heaters[left]), abs(heaters[right] - house))


    # approach 2: two pointers
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()
    i, j = 0, 0
    min_radius = 0
    while(i < len(houses) and j < len(heaters)):
        curr_radius = abs(houses[i] - heaters[j])
        next_radius = abs(houses[i] - heaters[j + 1]) if j + 1 < len(heaters) \
        else float('inf')
        
        if curr_radius < next_radius:
            min_radius = max(curr_radius, min_radius)
            i += 1
        else:
            j += 1
        
    return min_radius
            