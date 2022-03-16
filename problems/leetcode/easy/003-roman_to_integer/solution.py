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
