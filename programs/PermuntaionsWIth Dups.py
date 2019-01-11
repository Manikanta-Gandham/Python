class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        print(res)
        return res


    def dfs(self, nums, path, res):
         if not nums:
            res.append(path)
        # return # backtracking
         for i in range(len(nums)):
            if  i> 0 and nums[i] == nums[i-1] :
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

sol = Solution()
sol.permuteUnique([1,2,3,4])