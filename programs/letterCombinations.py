# def letterCombinations(self, digits):
#     dic = {"1":[], "2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6": ["m", "n", "o"],
#           "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}
#     def h(digits):
#         if not digits: return []
#         m = len(digits)/2
#         if not m: return dic[digits[0]]
#         return [ c+cc for c in h(digits[:m]) for cc in h(digits[m:]) ]
#     return h(digits)