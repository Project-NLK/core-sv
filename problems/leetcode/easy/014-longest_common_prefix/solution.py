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

    def longestCommonPrefixBest(self, strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        shorts = min(strs)
        longs = max(strs)

        for i in range(len(shorts)):
            if shorts[i] != longs[i]:
                return shorts[:i]

        return shorts
