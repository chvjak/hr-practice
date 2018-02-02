class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        N = len(S)  # S = ababc
        ixs = [i for i in range(N)]

        ixs.sort(key=lambda x: S[x])  # ixs = 0,2,1,3,4

        # first and last index of a letter {'a':[0,2], ...}
        flil = {}

        ix_prev = None
        for ix in ixs:
            c = S[ix]

            if c not in flil.keys():
                flil[c] = [ix, ix]
            else:
                flil[c][1] = ix

        res = []

        # find max last index
        ix = 0
        fi, li = flil[S[ix]]
        max_last_index = li

        while ix < N:
            while ix <= max_last_index:
                fi, li = flil[S[ix]]
                max_last_index = max(max_last_index, li)
                ix += 1


            res.append(max_last_index)
            if ix == N:
                break

            fi, li = flil[S[ix]]
            max_last_index = max(max_last_index, li)

        #print([S[s+1:e] for s, e in zip([-1] + res[:-1], res)])
        return [e - s for s, e in zip([-1] + res[:-1], res)]

S = Solution()
print(S.partitionLabels("ababcbacadefegdehijhklij"))
print(S.partitionLabels("caedbdedda"))