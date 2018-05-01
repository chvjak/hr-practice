

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''


# Your task is to complete this function
# Function should return an integer
def maxCoins(arr, n):
    # Code here

    cache = {}
    def maxCoinsDP(lix, rix, x_move):
        if lix == rix:
            if x_move:
                return (arr[lix], 0)
            else:
                return (0, arr[lix])

        if (lix, rix, x_move) in cache.keys():
            return cache[(lix, rix, x_move)]

        x_score1, y_score1 = maxCoinsDP(lix + 1, rix, not x_move)
        if x_move:
            x_score1 += arr[lix]
        else:
            y_score1 += arr[lix]

        x_score2, y_score2 = maxCoinsDP(lix, rix - 1, not x_move)
        if x_move:
            x_score2 += arr[rix]
        else:
            y_score2 += arr[rix]

        if x_move:
            if x_score1 > x_score2:
                x_score = x_score1
                y_score = y_score1
            else:
                x_score = x_score2
                y_score = y_score2
        else:
            if y_score1 > y_score2:
                x_score = x_score1
                y_score = y_score1
            else:
                x_score = x_score2
                y_score = y_score2

        cache[(lix, rix, x_move)] = (x_score, y_score)
        return (x_score, y_score)

    N = len(arr)
    x_score, y_score = maxCoinsDP(0, N - 1, True)

    return x_score


# Driver Program
if __name__ == '__main__':
    f = open('pots_of_gold.txt')
    t = int(f.readline().strip())
    for i in range(t):
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
        print(maxCoins(arr, n))
    # Contributed By: Harshit Sidhwa

