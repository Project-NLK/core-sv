# Longest Common Prefix

> 문제 링크: https://leetcode.com/problems/longest-common-prefix/

## 문제

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Example 1

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

### Example 2

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

### Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lower-case English letters.

### Follow-up

- 없음

---

## 문제 분석

### 문제 해석

문자열 배열 중에서 가장 긴 공통된 접두사를 찾아라. 만약 공통된 접두사가 없다면 빈 문자열을 반환하라

### 문제 정리

- 모든 문자열 배열에 공통되는 접두사를 찾아야 함

### 엣지 케이스

- 공통되는 접두사가 없을 경우

### 풀이 & 시간복잡도 / 공간복잡도

- 정렬을 해서 첫 번째 문자열과 마지막 문자열을 비교해서 얻을 수 있음
  - 이 방법은 sorting으로 인해 $O(nlog(n))$의 시간복잡도를 가질 것으로 추측
- 방법
  - 전체 문자열을 순회
  - 첫 번째 문자열을 prefix로 저장
  - 인덱스 1부터 마지막까지 순회하면서 prefix를 갱신
  - 만약 갱신 중 빈 문자열이 나올 경우 반환
  - 시간복잡도
    - 이번 문제에서 가변 값은 strs의 길이, str의 길이
    - strs의 길이를 n, str의 길이를 k라고 가정
    - $O(nk)$
  - 공간복잡도
    - 정답만 반환하기 위한 메모리 사용
    - $O(1)$

---

## 소스 코드

```python
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = strs[0]

        for value in strs[1:]:
            answer = self.findLongestCommonPrefix(answer, value)

            if answer == "":
                break

        return answer

    def findLongestCommonPrefix(self, str1, str2) -> str:
        answer = ""
        shortStr, longStr = str1, str2

        if len(shortStr) > len(longStr):
            shortStr, longStr = longStr, shortStr

        for i in range(0, len(shortStr)):
            if shortStr[i] == longStr[i]:
                answer += shortStr[i]
            else:
                break

        return answer
```

---

## 실행 결과

![Screen Shot 2022-03-16 at 8.51.35 PM.png](images/image-01.png)

---

## Best Practice

```python
class Solution:
    def longestCommonPrefix(self, m):
        if not m: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(m)
        s2 = max(m)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
```

- 문자열의 `min`/`max`는 문자열 크기를 기준으로 찾아줌
- 가장 큰 값과 가장 작은 값을 가지고 와서 비교
- 시간복잡도
  - min 값과 max 값을 찾아오는 로직이 $2n$
  - 문자열 중 가장 짧은 문자열 길이에 대한 시간복잡도
  - $O(nk)$ → 이때 k는 가장 짧은 문자열 길이

---

## 관련 학습

- `str` 자료형에서 `min` / `max` 함수는 길이가 아닌 크기를 기준으로 조회
  - 문자열의 크기를 기준으로 조회함
  - 만약 길이를 기준으로 조회하고 싶은 경우 `min(str, key=len)`과 같이 사용해야 함

---

## 참고 자료

[beat 100% python submission, short and clean - LeetCode Discuss](https://leetcode.com/problems/longest-common-prefix/discuss/172553/beat-100-python-submission-short-and-clean)

[How does the max() function work on list of strings in python?](https://stackoverflow.com/questions/20463204/how-does-the-max-function-work-on-list-of-strings-in-python)

[Python - 최소값, 최대값 (min, max)](https://codechacha.com/ko/python-min-max/)

[TimeComplexity - Python Wiki](https://wiki.python.org/moin/TimeComplexity)
