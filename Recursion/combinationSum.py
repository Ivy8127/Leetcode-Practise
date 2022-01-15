#Time complexity - O(n + k)! n - size of candidates k max repeated time for each candidate
def combinationSum(candidates, target):
    result = []
    combinations = []
    candidates.sort()
    return dfs(candidates,target,combinations,result)

def dfs(candidates,target,combinations,result):
    if target == 0:
        result.append(combinations)
        return
    if target < 0:
        return

    for i in range(len(candidates)):
        if candidates[i] > target :
            break
        else:
            dfs(candidates[i:],target-candidates[i],combinations+[candidates[i]],result)

    return result

print(combinationSum([2,3,6,7],7))            
