
class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(1,n):
            if arr[i] >= arr[i-1]:
                pass
            else:
                return 0
        return 1
