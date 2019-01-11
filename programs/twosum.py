class Solution:
    def twoSum(self, array, target):
        dictionary = {}
        for i in range(len(array)):
            required = target - array[i]
            if required in dictionary:
                print(dictionary[required], i)
                return [dictionary[required], i]
            else:
                dictionary[array[i]] = i
        return 0

a = Solution()
a.twoSum([5,2,7], 9)