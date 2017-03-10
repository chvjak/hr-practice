file = open('markov-snakes-and-ladders.txt')
def input():
    return file.readline()


class Dice:
    def __init__(self, weights):
        weights = [int(f * 100) for f in weights]
        LW = len(weights) # 6
        cum_weights = [0] * LW
        cum_weights[0] = weights[0]
        for i in range(1, LW):
            cum_weights[i] += cum_weights[i - 1] + weights[i]

        val = 1
        vals = [0] * 100
        j = 0
        for i in range(100):
            vals[i] = val
            if i > cum_weights[j]:
                val += 1
                j += 1


        self.vals = vals


    def roll(self):
        import random
        rval = random.randrange(100)
        return self.vals[rval]


def simulate(board, dice):
    pos = 1

    roll_count = 0
    while pos < 100:
        new_pos = pos + dice.roll()
        if new_pos <= 100:
            pos = board[new_pos]  # what if pos + roll > 100?

        roll_count += 1

    return roll_count


N = int(input())

for i in range(N):
    s = input()
    probs = [float(x) for x in s.strip().split(',')]

    ladders_count, snakes_count = [int(x) for x in input().strip().split(',')]
    ladders = [x.split(',') for x in input().strip().split(' ')]
    snakes = [x.split(',') for x in input().strip().split(' ')]

    board = list(range(0, 101))
    for (f, t) in ladders + snakes:
        board[int(f)] = int(t)

    dice_roll_count = 0
    samples = 100
    for i in range(samples):
        dice_roll_count += simulate(board, Dice(probs))
    print(int(dice_roll_count / samples))



