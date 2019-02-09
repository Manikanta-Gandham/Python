class Solution:
    def isAnagram(self, anagram1, anagram2):
        dict1 = {}
        dict2 = {}
        for a1 in anagram1:
            dict1[a1] = dict1.get(a1) + 1 if dict1.get(a1) else 1

        for a2 in anagram2:
            dict2[a2] =  dict2.get(a2) + 1 if dict2.get(a2) else 1

        return dict1 == dict2
sol = Solution()
print(sol.isAnagram("abc","abc"))