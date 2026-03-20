class Solution:
    def selectionSort(self, nums):

        n = len(nums)
        for i in range (0,n-1):
            mini = i

            for j in range (i+1, n):
                if nums[j] < nums[mini]:
                    mini = j

            nums[i], nums[mini] = nums[mini], nums[i]
        
        return nums

