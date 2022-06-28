class Solution:
    def sortIntegers(self, s):
        if not s:
            return

        temp = [0] * len(s)
        self.mergeSort(temp, 0, len(s) - 1)

    def mergeSort(self, s, start, end, temp):
        if start >= end:
            return
        mid = start + (end - start) // 2

        self.mergeSort(s, start, mid, temp)
        self.mergeSort(s, mid, end, temp)
        self.merge(s, start, end, temp)

    def merge(self, s, start, end, temp):
        mid = start + (end - start) // 2
        leftStart = start
        rightStart = mid + 1
        index = leftStart

        while leftStart <= mid and rightStart <= end:
            if (s[leftStart] < s[rightStart]):
                temp[index] = temp[leftStart]
                index += 1
                leftStart += 1

            else:
                temp[index] = temp[rightStart]
                index += 1
                rightStart += 1

            while(leftStart <= mid):
                temp[index] = s[leftStart]
                index += 1
                leftStart += 1

            while(rightStart <= end):
                temp[index] = temp[rightStart]
                index += 1
                rightStart += 1

            for i in range(start, end+1):
                s[i] = temp[i]
