class Solution:
    def Urilify(self, str1):
        strList = list(str1) # though of using this but strList = str1.split() split is ["mani","is","good","boy"] split is based on empty space
        print(strList)
        for i in range(len(strList)):
            if strList[i] == " ":  #  or strList[]
                strList = strList[:i] + ["%d20"] + strList[i+1:]
        return "".join(strList)

sol = Solution()
print(sol.Urilify("Mani is a good boy"))