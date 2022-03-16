# Roman to Integer

> 문제 링크: https://leetcode.com/problems/roman-to-integer/

## 문제

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
Symbol        Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two one's added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Example 1

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

### Example 2

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

### Example 3

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

### Contraints

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

### Follow-up

- 없음

---

## 문제 분석

### 문제 해석

로마 숫자는 7개의 다른 기호로 표현된다: `I`, `V`, `X`, `L`, `C`, `D`, 그리고 `M`

```
Symbol        Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

예를 들어, `2`는 로마 숫자로는 `II`로 표현할 수 있는데, 단지 두 개의 1을 서로 더한 것이다. `12`는 `XII`로 쓰여지는데 단순하게 `X + II` 이다. `27`은 `XXVII`로 쓰여지는데, `XX + V + II` 이다.

로마 숫자는 대게 큰 값에서부터 작은 값이 왼쪽에서 오른쪽으로 쓰여진다. 그러나, 숫자 4는 `IIII`가 아니다. 대신에 `IV`로 쓰여진다. 왜냐하면 1은 5보다 앞에 있기 때문에 빼서 4가 된다. 같은 원리가 숫자 9에도 적용되는데, `IX`로 쓰여진다. 빼기가 사용되는 경우가 6가지 존재한다

- `I`는 `V`와 `X` 앞에 와서 5와 9를 만든다.
- `X`는 `L`과 `C` 앞에 와서 40과 90을 만든다.
- `C`는 `D`와 `M` 앞에 와서 400과 900을 만든다.

주어진 로마 숫자를 정수로 변경하라

### 문제 정리

- 로마 숫자를 정수로 변환해야 함
- 특정 심볼을 여러번 반복해서 특정한 정수로 표현 가능
- 6가지 특수 케이스의 경우 앞에 배치해서 뺄셈으로 숫자를 표현
  - 큰 수 표현 심볼 앞에 작은 수 표현 심볼이 존재한다면 뺄셈을 해야 함

### 엣지 케이스

- 6가지 특수 케이스

### 풀이 & 시간복잡도 / 공간복잡도

- 최대 3999라면 → MMMCMXCIX
- 이전 심볼을 기억하고 만약 이전 심볼보다 현재 심볼이 더 큰 값이 들어올 경우 확인 필요
  - C(D, M), X(L, C), I(V, X)
- 풀이
  - 3개의 변수를 관리
    - 전체 결과, 이전 심볼, 현재 심볼
  - 이전 심볼을 결과에 연산하는 시점은 현재 심볼 조회 이후
  - 현재 심볼이 이전 심볼보다 클 때
    - 이전 심볼을 결과에서 뺌
  - 현재 심볼이 이전 심볼보다 같거나 작을 때
    - 이전 심볼을 결과에 더함
  -

---

## 소스 코드

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if len(s) == 1:
            return symbols[s]

        answer = 0
        pre = symbols[s[0]]

        for symbol in s[1:]:
            current = symbols[symbol]
            if pre < current:
                answer, pre = answer - pre, current
                continue
            answer, pre = answer + pre, current

        return answer + current
```

---

## 실행 결과

![Screen Shot 2022-03-09 at 9.33.20 PM.png](images/image-01.png)

---

## Best Practice

```python
class Solution:
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
```

---

## 참고 자료

[My Straightforward Python Solution - LeetCode Discuss](https://leetcode.com/problems/roman-to-integer/discuss/6537/My-Straightforward-Python-Solution)
