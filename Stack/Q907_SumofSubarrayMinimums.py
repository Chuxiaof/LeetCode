class Solution:

    # O(n**2)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sum_stack = 0
        sum_min = 0
        
        for idx,num in enumerate(arr):
            while stack and num < stack[-1]:  
                sum_stack -= stack.pop()
             
            while len(stack) < idx+1:
                stack.append(num)
                sum_stack += num
                
            sum_min += sum_stack
         
        return sum_min % 1000000007
                

    # O(n)

    def sumSubarrayMins2(self, arr: List[int]) -> int:
        stack = []
        sum_stack = 0
        sum_min = 0
        
        for idx, num in enumerate(arr):
            popped = 0
            while stack and num < stack[-1][1]: 
                count, perv_num = stack.pop()
                sum_stack -= count * perv_num
                popped += count
            count = popped + 1
            if count > 0:
                stack.append((count, num))
                sum_stack += count * num
                
            sum_min += sum_stack
         
        return sum_min % 1000000007
                
            
            
        
  