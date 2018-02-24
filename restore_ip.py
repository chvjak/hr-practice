

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def restoreIP(ix = 0, pc=3, prev_pix=-1):

            if pc == 0 and N - 3 <= ix <= N - 1 and int(s[ix:]) < 256:
                if ix == N - 1 or s[ix] != '0':
                    return [s[ix:]]
                else:
                    return []

            if ix == N or pc == 0:
                return []

            if int(s[prev_pix + 1:ix + 1]) >= 256:
                return []

            if (ix - prev_pix > 1) and s[prev_pix + 1] == '0':
                return []

            res = []

            r1 = restoreIP(ix + 1, pc - 1, ix)  # place point

            r2 = restoreIP(ix + 1, pc, prev_pix)

            for r in r1:
                res.append(s[ix] + '.' + r)

            for r in r2:
                res.append(s[ix] + r)

            return res

        N = len(s)

        res = restoreIP()

        return res


S = Solution()
print(S.restoreIpAddresses("010010"))
print(S.restoreIpAddresses("333333"))
print(S.restoreIpAddresses("1111111"))
print(S.restoreIpAddresses("2222222"))
print(S.restoreIpAddresses("25525511135"))

print(S.restoreIpAddresses("1111"))
print(S.restoreIpAddresses("1234567"))
print(S.restoreIpAddresses("12345678"))
