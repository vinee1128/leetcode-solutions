class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007

        dp = [0] * 26
        total = 0

        for ch in s:
            i = ord(ch) - ord('a')

            new_subseq = total + 1

            total = (total + new_subseq - dp[i]) % MOD

            dp[i] = new_subseq

        return total
