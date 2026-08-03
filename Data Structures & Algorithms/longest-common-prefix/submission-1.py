class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        short = strs[0]
        long = strs[-1]

        for i in range(len(short)):
            if short[i] != long[i]:
                return short[:i]

        return short
        