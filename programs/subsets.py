class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res, 0)
        print(res)
        return res


    def dfs(self, nums, path, res, start):
         res.append(path)
        # return # backtracking
         for i in range(start, len(nums)):
            if  i> 0 and nums[i] == nums[i-1] :
                continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res, i+1)

sol = Solution()
sol.permuteUnique([1,2,3])