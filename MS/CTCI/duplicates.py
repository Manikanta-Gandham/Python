class Solution:
    def isDup(self, strArg = "abcdabcd"):
        arg = list(strArg)
        arg.sort()
        for i in range(len(arg)):
            if arg[i]  == arg[i-1]:
                return False
        return True

sol = Solution()
print(sol.isDup("abc"))
