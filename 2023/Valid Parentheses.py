class Solution:
    def  isValid(self, s: str) -> bool:
        # Wrong Solution "([)]" reurned True but actual value if false
        # dic = {}
        # dic = {'[': 0, ']': 0, '(': 0, ')': 0, '{': 0, '}':0}
        # for c in s:
        #     dic[c] = dic[c] + 1
        #     if (dic[']'] > dic['[']) or (dic[')'] > dic['(']) or (dic['}'] > dic['{']) :
        #        return False
        # if (dic[']'] != dic['[']) or  (dic[')'] != dic['(']) or (dic['}'] != dic['{']) :
        #     return False
        
        # return True
    
        stack = []
        dic = {'(': ')','{': '}','[': ']'}
        for c in s:
            if c in dic:
                stack.append(c)
            else :
                if len(stack) == 0 or dic[stack.pop()] != c:
                    return False
        if(len(stack))!= 0:
            return False
        return True

sol = Solution()
if(sol.isValid('()')== True):
    print(True)