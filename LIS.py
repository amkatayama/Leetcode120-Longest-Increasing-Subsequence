class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # creating a cache array 
        sol = [0] * len(nums)

        for i in range(len(nums)):
            s = i  # starting point 
            length = 1  # initializing length of LIS
            for j in range(i+1, len(nums)):
                # if the subsequent integer is smaller then do nothing
                if nums[j] <= nums[s]:
                    continue
                # increase the length of LIS, and update starting point if the subsequent element is larger 
                length += 1 
                s = j
            sol[i] = length
        
        return max(sol)
