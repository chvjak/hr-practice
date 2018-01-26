import sys
def buy(cache, A, si):
    res1 = sell(cache, A, si + 1, A[si])
    res2 = wait(cache, A, si + 1, A[si])

    return max(res1, res2)


def sell(cache, A, si, buy_price):
    N = len(A)

    res1 = A[si] - buy_price
    res1 += wait(cache, A, si + 1)

    if N > si + 1:
        res2 = wait(cache, A, si + 1, buy_price)
    else:
        res2 = -buy_price

    return max(res1, res2)


def wait(cache, A, si = 0, buy_price_or_none = None):
    N = len(A)


    if N < si + 2:
        if N == si + 1 and buy_price_or_none is not None:
            return sell(cache, A, si, buy_price_or_none)
        else:
            if buy_price_or_none is not None:
                return -buy_price_or_none
            else:
                return 0

    if buy_price_or_none in cache[si].keys():
        return cache[si][buy_price_or_none]


    if buy_price_or_none is None:
        res1 = buy(cache, A, si)
    else:
        res1 = sell(cache, A, si, buy_price_or_none)

    res2 = wait(cache, A, si + 1)

    cache[si][buy_price_or_none] = max(res1, res2)
    return cache[si][buy_price_or_none]


def maxProfitDP(A):
    N = len(A)
    cache = [{} for _ in range(N)]

    res = wait(cache, A)

    return res


def maxProfitTabulated(A):
    N = len(A)
    cache = [[None] * N for _ in range(N)]

    for i in range(N - 1):
        for j in range(i + 1, N):
            cache[i][j] = max(0, A[j] - A[i])       # profit if sold on day j what was bought on day i

    for i in reversed(range(N - 1)):
        max1 = 0
        for j in reversed(range(i + 1, N)):
            if j < N - 1:
                cache[i][j] = max(max1, cache[i][j] + cache[j][j + 1])

            max1 = max(max1, cache[i][j])

    return cache[0][1]


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        res = 0
        for i in range(len(A) - 1):
            if A[i + 1] - A[i] > 0:
                res += A[i + 1] - A[i]


        return res


    def maxProfitTab(self, A):
        res = maxProfitTabulated(A)

        return res

    def maxProfitDP(self, A):
        res = maxProfitDP(A)

        return res



S = Solution()


p = [1, 4, 5, 4, 10]
print(S.maxProfit(p))
print(S.maxProfitDP(p))


p = [3, 2, 1, 4, 5, 4, 10]
print(S.maxProfit(p))
print(S.maxProfitDP(p))


p = [10, 9, 11, 9, 8, 10, 7, 6, 8]
print(S.maxProfit(p))
print(S.maxProfitDP(p))

p = [2, 1, 10, 2, 10, 3, 10]
print(S.maxProfit(p))
print(S.maxProfitDP(p))




print(S.maxProfit([1461183, 6525292, 432883, 7905638, 6458495, 9679177, 4781402, 1690866, 9998475, 9545879, 385101, 7952372, 253059, 7839218, 7056331, 2048851, 996911, 972169, 6975165, 3711763, 7170345, 3523755, 1691692, 5753412, 8958613, 3823651, 5289477, 3054221, 6693439, 9468345, 8811765, 3975815, 9676674, 1940055, 9621052, 134090, 1390939, 3472763, 2950316, 1313761, 3260911, 5951772, 2610357, 2983782, 7840589, 7900872, 2176078, 4223970, 6936119, 7404095, 7408193, 3551259, 1335802, 9277645, 4559010, 1825826, 5060019, 7813150, 293916, 8052411, 3922659, 8039787, 1627888, 8949155, 645406, 8170870, 3966219, 2847254, 9071852, 461992, 3936386, 4151866, 904049, 3776743, 4390232, 8176157, 7453409, 5540516, 945511, 8167163, 6051601, 9693372, 1220501, 6699510, 3965370, 9088052, 1992544, 7174997, 1709911, 6558095, 1390354, 4236440, 6605220, 9774047, 4270248, 5620652, 8558170, 9736836, 4924436, 7529032, 9501045, 3385305, 3461575, 6368652, 4911993, 9142373, 8851269, 6077729, 6806823, 6260409, 9773288, 6590653, 8979321, 254106, 9119641, 3535194, 9195133, 5650112, 905498, 4330147, 1802496, 3106581, 4982564, 8279778, 4670897, 7141310, 5005183, 9358147, 3516387, 3523633, 4208216, 3497259, 6993062, 3291244, 6052946, 3692205, 9379946, 3065700, 2291373, 9960652, 5788750, 7961236, 3889491, 198551, 4400143, 7334886, 6673991, 8983958, 386011, 8207216, 3672841, 7280840, 6518604, 8051899, 1044992, 3752874, 5035128, 4687732, 5728811, 9467637, 6563087, 3363310, 4650909, 1295248, 1934898, 4936159, 1972904, 1358033, 6443687, 2372619, 2404921, 7913370, 3089205, 4607856, 6635232, 3497688, 2871455, 2250963, 5572272, 8646540, 4755832, 665722, 3716278, 6289111, 5101645, 2755280, 2166061, 4622291, 1171832, 1543942, 8695254, 1239265, 3343006, 1241153, 1483344, 8629076, 3288823, 2840246, 2411554, 284454, 215740, 4921940, 1840439, 752906, 5272512, 1097051, 6541549, 3811699, 6904581, 1175921, 1722791, 4542095, 8548545, 74715, 9945752, 109505, 4096455, 2637972, 9779442, 8651720, 8348033, 555587, 3218066, 7071297, 2545073, 3023691, 1145044, 6155323, 1192935, 1237332, 3261594, 3723236, 7528909, 3222912, 4988348, 298098, 537131, 8307295, 9285312, 4431361, 1297158, 7511099, 4509869, 6214005, 751208, 6169461, 8245510, 7992247, 4464936, 8416361, 1043018, 5505726, 5641052, 8695706, 6282069, 7931522, 5554661, 8177347, 1965885, 1130246, 3977311, 7582565, 3232295, 2301698, 1418279, 7960793, 1072580, 2384819, 5546941, 7420614, 4711112, 5913810, 3459940, 6985850, 2103392, 1050019, 5872531, 334456, 5313692, 8758706, 8087858, 5640727, 5486114, 5015495, 7687218, 6965953, 727442, 5433139, 9502011, 4519729, 8425566, 9674599, 1724732, 4199584, 671932, 3459148, 6259276, 3192303, 8498916, 564565, 1735390, 5875749, 300726, 1617804, 2997046, 6287469, 9849852, 7643547, 4000624, 2933779, 9103947, 8636627, 3937186, 1034906, 358503, 3620840, 6774954, 9484424, 568135, 3547513, 2262555, 7992481, 2879313, 109484, 4308276, 9324162, 4110685, 4447739, 6089630, 1363278, 1778942, 1212532, 6564477, 1415239, 7610339, 5401277, 4918304, 7138919, 7993207, 4817309, 102838, 9791515, 1918716, 4303904, 8723028, 227907, 7338059, 2378503, 8062131, 6304197, 3636717, 2815233, 330190, 2902825, 2543616, 3342537, 8165314, 1175524, 1637191, 7975061, 2802412, 1704717, 9231543, 9575330, 9818546, 2637413, 973317, 9504768, 8898435, 3836136, 4357810, 767309, 7196659, 5372174, 3175443, 7152725, 6083245, 1558246, 5572895, 7723879, 7105308, 1460100, 6776059, 3961726, 9120330, 8196552, 9845425, 298290, 9546421, 593421, 2647923, 4263260, 8645895, 4990025, 177738, 8806959, 3882590, 1721108, 2370148, 5030871, 2428128, 6823844, 3670919, 3645980, 6098332, 5690198, 830896, 3527354, 12834, 1041424, 1060274, 3267823, 7075831, 1890951, 1481752, 8072398, 4411112, 6319440, 5964244, 8759190, 8088413, 6779750, 4955, 7968485, 3703621, 4391586, 3486792, 2056696, 4597340, 6038072, 8806049, 6243318, 8190784, 9783931, 1729211, 3302286, 3803066, 5020713, 2893787, 3545248, 9419065, 1785038, 1555972, 6610960, 991247, 1443235, 4400739, 7554130, 9604565, 7990802, 3297551, 7511927, 5670225, 9595256, 2694993, 322363, 6664248, 5055320]))
print(S.maxProfit([10, 11, 15, 14, 13, 10, 9, 12, 13]))
print(S.maxProfit([10, 15, 14, 13, 10, 9, 12, 13]))
print(S.maxProfit([9, 12, 13]))
print(S.maxProfit([10, 15, 11, 12]))
print(S.maxProfit([5, 1, 10]))

print()

print(S.maxProfitDP([1461183, 6525292, 432883, 7905638, 6458495, 9679177, 4781402, 1690866, 9998475, 9545879, 385101, 7952372, 253059, 7839218, 7056331, 2048851, 996911, 972169, 6975165, 3711763, 7170345, 3523755, 1691692, 5753412, 8958613, 3823651, 5289477, 3054221, 6693439, 9468345, 8811765, 3975815, 9676674, 1940055, 9621052, 134090, 1390939, 3472763, 2950316, 1313761, 3260911, 5951772, 2610357, 2983782, 7840589, 7900872, 2176078, 4223970, 6936119, 7404095, 7408193, 3551259, 1335802, 9277645, 4559010, 1825826, 5060019, 7813150, 293916, 8052411, 3922659, 8039787, 1627888, 8949155, 645406, 8170870, 3966219, 2847254, 9071852, 461992, 3936386, 4151866, 904049, 3776743, 4390232, 8176157, 7453409, 5540516, 945511, 8167163, 6051601, 9693372, 1220501, 6699510, 3965370, 9088052, 1992544, 7174997, 1709911, 6558095, 1390354, 4236440, 6605220, 9774047, 4270248, 5620652, 8558170, 9736836, 4924436, 7529032, 9501045, 3385305, 3461575, 6368652, 4911993, 9142373, 8851269, 6077729, 6806823, 6260409, 9773288, 6590653, 8979321, 254106, 9119641, 3535194, 9195133, 5650112, 905498, 4330147, 1802496, 3106581, 4982564, 8279778, 4670897, 7141310, 5005183, 9358147, 3516387, 3523633, 4208216, 3497259, 6993062, 3291244, 6052946, 3692205, 9379946, 3065700, 2291373, 9960652, 5788750, 7961236, 3889491, 198551, 4400143, 7334886, 6673991, 8983958, 386011, 8207216, 3672841, 7280840, 6518604, 8051899, 1044992, 3752874, 5035128, 4687732, 5728811, 9467637, 6563087, 3363310, 4650909, 1295248, 1934898, 4936159, 1972904, 1358033, 6443687, 2372619, 2404921, 7913370, 3089205, 4607856, 6635232, 3497688, 2871455, 2250963, 5572272, 8646540, 4755832, 665722, 3716278, 6289111, 5101645, 2755280, 2166061, 4622291, 1171832, 1543942, 8695254, 1239265, 3343006, 1241153, 1483344, 8629076, 3288823, 2840246, 2411554, 284454, 215740, 4921940, 1840439, 752906, 5272512, 1097051, 6541549, 3811699, 6904581, 1175921, 1722791, 4542095, 8548545, 74715, 9945752, 109505, 4096455, 2637972, 9779442, 8651720, 8348033, 555587, 3218066, 7071297, 2545073, 3023691, 1145044, 6155323, 1192935, 1237332, 3261594, 3723236, 7528909, 3222912, 4988348, 298098, 537131, 8307295, 9285312, 4431361, 1297158, 7511099, 4509869, 6214005, 751208, 6169461, 8245510, 7992247, 4464936, 8416361, 1043018, 5505726, 5641052, 8695706, 6282069, 7931522, 5554661, 8177347, 1965885, 1130246, 3977311, 7582565, 3232295, 2301698, 1418279, 7960793, 1072580, 2384819, 5546941, 7420614, 4711112, 5913810, 3459940, 6985850, 2103392, 1050019, 5872531, 334456, 5313692, 8758706, 8087858, 5640727, 5486114, 5015495, 7687218, 6965953, 727442, 5433139, 9502011, 4519729, 8425566, 9674599, 1724732, 4199584, 671932, 3459148, 6259276, 3192303, 8498916, 564565, 1735390, 5875749, 300726, 1617804, 2997046, 6287469, 9849852, 7643547, 4000624, 2933779, 9103947, 8636627, 3937186, 1034906, 358503, 3620840, 6774954, 9484424, 568135, 3547513, 2262555, 7992481, 2879313, 109484, 4308276, 9324162, 4110685, 4447739, 6089630, 1363278, 1778942, 1212532, 6564477, 1415239, 7610339, 5401277, 4918304, 7138919, 7993207, 4817309, 102838, 9791515, 1918716, 4303904, 8723028, 227907, 7338059, 2378503, 8062131, 6304197, 3636717, 2815233, 330190, 2902825, 2543616, 3342537, 8165314, 1175524, 1637191, 7975061, 2802412, 1704717, 9231543, 9575330, 9818546, 2637413, 973317, 9504768, 8898435, 3836136, 4357810, 767309, 7196659, 5372174, 3175443, 7152725, 6083245, 1558246, 5572895, 7723879, 7105308, 1460100, 6776059, 3961726, 9120330, 8196552, 9845425, 298290, 9546421, 593421, 2647923, 4263260, 8645895, 4990025, 177738, 8806959, 3882590, 1721108, 2370148, 5030871, 2428128, 6823844, 3670919, 3645980, 6098332, 5690198, 830896, 3527354, 12834, 1041424, 1060274, 3267823, 7075831, 1890951, 1481752, 8072398, 4411112, 6319440, 5964244, 8759190, 8088413, 6779750, 4955, 7968485, 3703621, 4391586, 3486792, 2056696, 4597340, 6038072, 8806049, 6243318, 8190784, 9783931, 1729211, 3302286, 3803066, 5020713, 2893787, 3545248, 9419065, 1785038, 1555972, 6610960, 991247, 1443235, 4400739, 7554130, 9604565, 7990802, 3297551, 7511927, 5670225, 9595256, 2694993, 322363, 6664248, 5055320]))
print(S.maxProfitDP([10, 11, 15, 14, 13, 10, 9, 12, 13]))
print(S.maxProfitDP([10, 15, 14, 13, 10, 9, 12, 13]))
print(S.maxProfitDP([9, 12, 13]))
print(S.maxProfitDP([10, 15, 11, 12]))
print(S.maxProfitDP([5, 1, 10]))