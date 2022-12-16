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

print(unique_paths(1,1))
print(unique_paths(2,2))
print(unique_paths(3,3))
print(unique_paths(4,4))
class UPTest(unittest.TestCase):
    def test_empty_input(self):
        x = unique_paths(0, 0)
        self.assertEqual(x, 0)

    def test_grids_inputs(self):
        g_inputs = [1,2,3,4]
        exp_results = [1,2,6,20]
        for i in range(len(g_inputs)):
            self.assertEqual(unique_paths(g_inputs[i],g_inputs[i]),  exp_results[i])