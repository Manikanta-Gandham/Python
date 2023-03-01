class Solution:
    def twoSum (self, l1, target):
        for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                if l1[i] + l1[j] == target:
                    return [l1[i], l1[j]]
        print("none")
        # O(N)^2
    def twoSum2(self, l1, target):
        dict  = {}
        for i in range(len(l1)):
            complement = target - l1[i]
            if dict.get(complement) != None:
                print(i, dict[complement])
                return [i, dict[complement]]

            else:
                dict[l1[i]]= i

        print("none")


sol = Solution()
sol.twoSum([2,3,7], 11)
sol.twoSum2([2,3,7], 10)

