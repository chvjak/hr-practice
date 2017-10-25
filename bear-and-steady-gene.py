f = open('bear-and-steady-gene.txt')
def input():
    return f.readline()

N = int(input().strip())
S = input().strip()

pfx_arr = [0] * N
pfx_dict = {'A': pfx_arr[:], 'C': pfx_arr[:], 'G': pfx_arr[:], 'T': pfx_arr[:]}
pfx_dict[S[0]][0] += 1
for i in range(1, N):
    pfx_dict['A'][i] = pfx_dict['A'][i - 1]
    pfx_dict['C'][i] = pfx_dict['C'][i - 1]
    pfx_dict['G'][i] = pfx_dict['G'][i - 1]
    pfx_dict['T'][i] = pfx_dict['T'][i - 1]

    pfx_dict[S[i]][i] += 1

# print(pfx_dict)


# target count
t_count_A = t_count_C = t_count_G = t_count_T = N // 4

# source count
s_count_A = pfx_dict['A'][N - 1]
s_count_C = pfx_dict['C'][N - 1]
s_count_G = pfx_dict['G'][N - 1]
s_count_T = pfx_dict['T'][N - 1]
min_len1 = 0
if s_count_A < t_count_A:
    min_len1 += t_count_A - s_count_A
if s_count_C < t_count_C:
    min_len1 += t_count_C - s_count_C
if s_count_G < t_count_G:
    min_len1 += t_count_G - s_count_G
if s_count_T < t_count_T:
    min_len1 += t_count_T - s_count_T


# print(min_len1)
def count_min_len():
    new_count_dict = {}
    if min_len1 == 0:
        return 0
    for win_len in range(min_len1, N):
        new_count_dict['A'] = t_count_A - (s_count_A - pfx_dict['A'][win_len - 1])
        new_count_dict['C'] = t_count_C - (s_count_C - pfx_dict['C'][win_len - 1])
        new_count_dict['G'] = t_count_G - (s_count_G - pfx_dict['G'][win_len - 1])
        new_count_dict['T'] = t_count_T - (s_count_T - pfx_dict['T'][win_len - 1])
        for i in range(N - win_len):
            if i > 0:
                new_count_dict[S[i - 1]] -= 1
                new_count_dict[S[i + win_len - 1]] += 1

            #print(new_count_dict)

            if new_count_dict['A'] < 0 or new_count_dict['C'] < 0 or new_count_dict['G'] < 0 or new_count_dict['T'] < 0:
                continue

            if win_len == sum(new_count_dict.values()):
                return win_len



print(count_min_len())
