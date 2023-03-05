class Solution:
    def Atoi (self, input):
        idx = 0
        length = len(input)
        Max = pow(2,32) -1
        Min = -pow(2,32)
        sign = 1
        result = 0
        while (idx < length and input[idx] ==" "):
            idx = idx +1
        if input[idx] in ('+','-'):
            sign = -1 if input[idx] == '-' else 1
            idx = idx +1
        
        while(idx <length):
            if(input[idx].isdigit()):
                if((result > Max//10) or (result == Max//10 and int(input[idx])>Max%10)):
                        return Max if sign == 1 else Min
                result = result*10 + int(input[idx])
                idx = idx + 1
            else:
             return sign*result
        return sign*result

sol = Solution()
# print(sol.Atoi(" -42"))
# print(sol.Atoi("42"))
# print(sol.Atoi("42H"))
# print(sol.Atoi("H42H"))
print(sol.Atoi(str(-(pow(2,32) +1))))

        







# Input: s = "42"
# Output: 42
# Input: s = "   -42"
# Output: -42
# Input: s = "4193 with words"
# Output: 4193