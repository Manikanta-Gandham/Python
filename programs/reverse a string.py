class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        low = 0
        high = len(s) - 1
        while low <= high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return  "".join(s)

sol = Solution()
print(sol.reverseString("abcdef"))