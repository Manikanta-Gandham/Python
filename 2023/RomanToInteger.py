class Solution:
    # I             1
    # V             5
    # X             10
    # L             50
    # C             100
    # D             500
    # M             1000
    def romanToInt(self,input):
        map = {'I':1, 'V':5, 'X': 10, 'C': 100, 'L': 50, 'D':500, 'M': 1000}
        total = map[input[0]]
        for i in range (1,len(input)):
            total = total + map[input[i]]
            if map[input[i-1]] < map[input[i]]:
                total = total - 2*map[input[i-1]]
        return total

sol = Solution()
if sol.romanToInt("CIX") ==109:
    print(True)
if sol.romanToInt("LVIII") ==58:
    print(True)
if sol.romanToInt("MCMXCIV") ==1994:
    print(True)