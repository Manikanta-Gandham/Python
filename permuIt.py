
def permute(nums):
    results = [[]]
    for n in nums:
        new_results = []
        for result in results:
            for i in range(len(result)+1):
                results.append(result[:i] + [n] + result[i:])   ###insert n
        results = results
    return results

print(permute([1,3,4]))