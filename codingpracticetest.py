global steps_max
import unittest
def unique_paths(m: int, n: int) -> int:
    memo = {}
    global steps_max
    
    def dfs(c_r, c_c, steps):
        if (c_r, c_c) in memo:
            return memo[(c_r, c_c)]
        if c_r >= m or c_c >= n:
            return 0
        if c_r == m - 1 and c_c == n - 1:
            return 1
        
        level_steps = dfs(c_r + 1, c_c, steps + 1) + dfs(c_r, c_c + 1, steps + 1)
        memo[(c_r, c_c)] = level_steps
        return level_steps
    return dfs(0, 0, 0)
steps_max = 0



def longest_sub_len(nums):
    res = [[]]
    memo = {}
    def dfs(i, curr):
        if curr in memo:
            return memo[curr]
        if i == len(nums):
            return
        res.append(curr + [nums[i]])
        dfs(i + 1, curr)
        dfs(i + 1, curr + [nums[i]])
        
    dfs(0, [])
    c_max = 0
    for element in res:
        if strictly_increasing(element):
            c_max = max(len(element), c_max)
    return c_max


def strictly_increasing(nums):
    if len(nums) < 2:
        return True
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            return False
    return True

class EmptyList(unittest.TestCase):
    def empty_input(self):
        x = unique_paths(0, 0)
        self.assertEqual(x, 0)


sub_list = [50,3,10,7,40,80]
#longest_sub_len(sub_list)




#print(unique_paths(100, 100))
