class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s[::-1]:
            if char == "b" or char == "c":
                stack.append(char)

            elif char == "a":
                if len(stack) < 2:
                    return False
                if stack.pop() != "b" or stack.pop() != "c":
                    return False
            else:
                return False

        return not stack
