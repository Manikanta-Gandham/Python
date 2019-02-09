class Solution:
    def palindrome(self, str):
        i = 0
        j = len(str) -1

        while(i<j):
            if str[i] == " ":
                i = i + 1
                continue # Reason for using continue is incase of double spaces code breaks  "M  M"
            if str[j] == " ":
                j = j-1
                continue
            if str[i] == str[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True
sol = Solution()
print(sol.palindrome("mani i    nam"))

