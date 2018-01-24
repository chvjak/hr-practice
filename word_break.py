class Trie1:
    def __init__(self):
        self.data = {}

    def add(self, word):
        cur_data = self.data
        for c in word:
            if c not in cur_data:
                cur_data[c] = {}
            cur_data = cur_data[c]
        else:
            cur_data['$'] = None

    def contains(self, word):
        cur_data = self.data
        for c in word:
            if c not in cur_data:
                return False
            cur_data = cur_data[c]
        else:
            return '$' in cur_data


class Trie:
    def __init__(self):
        self.data = set()

    def add(self, word):
        self.data.add(word)

    def contains(self, word):
        return word in self.data


def can_be_broken(cache, string, si, tdict):
    #print(string[si:], len(string[si:]))

    N = len(string)

    if N == si:
        return True

    if cache[si] is not None:
        return cache[si]


    for i in range(N - si + 1):
        word = string[si:si + i]
        if tdict.contains(word):
            if can_be_broken(cache, string, si + i, tdict):
            #    print(word + ' found AND ' + string[si + i:] + ' can be broken')
                cache[si] = True
                return True
            #else:
            #    print(word + ' found BUT ' + string[si + i:] + ' cant be broken')

    cache[si] = False
    return False


def can_be_broken_tab(string, tdict):
    N = len(string)
    cache = [None] * (N + 1)    # if the string starting at i can be broken

    cache[N] = True         # Empty suffix can be broken

    for si in reversed(range(N)):
        for i in range(si, N):
            word = string[si:i + 1]
            if tdict.contains(word):
                cache[si] = cache[i + 1]
                if cache[si]:
                    break
            else:
                cache[si] = False

    return cache[0]


class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreakDP(self, string, dictionary):
        tdict = Trie()
        for w in dictionary:
            tdict.add(w)

        cache = [None] * len(string)
        res = can_be_broken(cache, string.strip(), 0, tdict)
        return 1 if res else 0


    def wordBreak(self, string, dictionary):
        tdict = Trie()
        for w in dictionary:
            tdict.add(w)

        res = can_be_broken_tab(string.strip(), tdict)
        return 1 if res else 0

S = Solution()


A = "babbb"
B = [ "baaaaaabba", "babbaababb", "abb", "bababaabab", "baaa", "ab", "ab", "bb", "abbaaaa", "bbababa", "bbbbbbab", "abbaaabba", "aaaabbab", "abaaab", "babab", "aabaaab", "aabaabbabb", "aa", "bb", "ab", "a", "a", "bbaaab", "aba", "ba", "bbabbaabab", "aaabbbbbb", "abbaaaabbb", "aabaabbaa", "bbba", "abbabbba", "abbbbabb", "bbaaba", "abbbbaab", "bba", "bbbbaabba", "ababbabaab", "baabba", "ababbaabb", "bbaab", "a", "bbba", "aaaa", "aaabbbabba", "bab", "baaaabaa", "ab", "aaabbaab", "bab", "aa", "ababababab", "aabbaaaba", "abbaaba", "bbaabaa" ]
print(S.wordBreakDP(A, B))
print(S.wordBreak(A, B))

A = "myinterviewtrainer "
B = [ "interview", "my", "trainer" ]
print(S.wordBreak(A, B))
print(S.wordBreakDP(A, B))
