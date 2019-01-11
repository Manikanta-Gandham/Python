class Solution:
    def myAtoi(self, str):
        array, res = list(str.strip()), 0
        if len(array) == 0:
            return 0
        sign = -1 if array[0]== "-" else 1
        if array[0] in ["-", "+"]: del array[0]
        for char in array:
            if not char.isdigit():break
            res = res*10 + int(char)
        if res < -2**31 :
            return -2**31
        elif res > 2**31:
            return 2**31
        else: return sign*res
sol = Solution()
sol.myAtoi("-1")