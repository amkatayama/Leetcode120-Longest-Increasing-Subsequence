class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # creating a cache array 
        sol = [0] * len(nums)

        for i in range(len(nums)):
            l = i  # left pointer 
            r = len(nums)-i-1  # right pointer 
            len_l, len_r = 1, 1 # length of LIS from the left and right 
            for j in range(r):
                # increase the length of LIS, and update starting point if the subsequent element is larger
                if nums[j+1] > nums[l]:
                    # shift the left pointer
                    l = j+1
                    len_l += 1
                if nums[len(nums)-j-2] < nums[r]:
                    # shift the right pointer
                    r = len(nums)-j-2
                    len_r += 1
                # if the subsequent integer is smaller then do nothing
 
            sol[i] = max(len_l, len_r)
        
        return max(sol)
