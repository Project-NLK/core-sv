class Solution(object):
    def brute_force(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def two_pass_hash_table(self, nums, target):
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if (target - num) in table and i != table[target - num]:
                return [i, table[target - num]]

    def one_pass_hash_table(self, nums, target):
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            else:
                table[num] = i


if __name__ == '__main__':
    solution = Solution()

    result1 = solution.brute_force([2, 7, 11, 15], 9)
    assert result1 == [0, 1] or [1, 0]

    result2 = solution.two_pass_hash_table([2, 7, 11, 15], 9)
    assert result2 == [0, 1] or [1, 0]

    result3 = solution.one_pass_hash_table([2, 7, 11, 15], 9)
    assert result3 == [0, 1] or [1, 0]
