
def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results
print(perms("abc"))

# def perms(word):
#     stack = list(word)
#     results = [""]
#     for letter in word:
#         new_results = []
#         for result in results:
#             for i in range(len(w)):
#                 new_results.append(w[:i] + letter + w[i:])
#         results = new_results
#     return results

