# 1. Two Sum

## Problem

> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> You can return the answer in any order.

## 문제

정수 배열 nums와 정수 target이 주어지고, 두 숫자를 더해서 target이 되는 숫자의 인덱스를 반환한다.

각 입력은 하나만 있다고 가정하고, 동일한 요소를 두번 사용할 수 없다.

답을 반환할 때 순서는 상관 없다.

## Example 1:

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Constraints

- 2 <= nums.length <= 104
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Solve & Complexity

### Brute force

가장 일반적인 방법으로 모든 경우의 수를 돌면서 체크한다.

```python
def brute_force(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

이중 루프로 인해 시간복잡도는 O(n^2)로 느리다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_brute_force_time_complexity.png" width="1000">

반면 별도의 메모리를 사용하지 않기 때문에 공간 복잡도는 O(n)으로 적다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_brute_force_space_complexity.png" width="1000">

### Hash Table - 1

해시 테이블(=딕셔너리)을 이용해 nums의 인덱스와 값을 미리 초기화해두고, 루프를 돌면서 해시 테이블의 값을 활용한다.

```python
def two_pass_hash_table(self, nums, target):
    table = {num: i for i, num in enumerate(nums)}

    for i, num in enumerate(nums):
        if (target - num) in table and i != table[target - num]:
            return [i, table[target - num]]
```

해시 테이블을 사용하는 부분은 시간 복잡도가 O(1)이지만 해시 테이블을 초기화하는 과정으로 인해 시간복잡도는 O(n)으로 빠르다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_two_pass_hash_table_time_complexity.png" width="1000">

해시 테이블을 사용하기 때문에 공간 복잡도는 높은 편이다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_two_pass_hash_table_space_complexity.png" width="1000">

### Hash Table - 2

`Hash Table - 1`에서는 해시 테이블을 초기화하는 과정과 nums를 탐색하는 과정으로 인해 루프를 2번 돌았는데, 이 부분을 한번으로 최적화한 풀이다.

```python
def one_pass_hash_table(self, nums, target):
    table = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in table:
            return [i, table[complement]]
        else:
            table[num] = i
```

시간 복잡도는 `Hash Table - 1`와 같이 O(n)이지만 루프를 한번으로 줄였기 때문에 `Hash Table - 1` 풀이보다 조금 더 빠르다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_one_pass_hash_table_time_complexity.png" width="1000">

이 풀이 역시 해시 테이블을 사용하기 때문에 공간 복잡도는 높은 편이다.

<img src="../../images/01.%20Two%20Sum/01_two_sum_one_pass_hash_table_space_complexity.png" width="1000">
