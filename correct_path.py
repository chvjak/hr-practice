def getPath(str1, pos=(0, 0), visited=set()):
    if pos == (4, 4) and len(str1) == 0:
        return True, ''

    if len(str1) == 0:
        return False, None

    if pos in visited:
        return False, None

    r, c = pos
    if not (0 <= r < 5) or not (0 <= c < 5):
        return False, None

    visited.add(pos)

    action_handlres = {'d': lambda: getPath(str1[1:], (r + 1, c), visited),
                       'u': lambda: getPath(str1[1:], (r - 1, c), visited),
                       'r': lambda: getPath(str1[1:], (r, c + 1), visited),
                       'l': lambda: getPath(str1[1:], (r, c - 1), visited)}

    if str1[0] == '?':
        actions = 'udlr'
    else:
        actions = str1[0]

    for a in actions:
        ok, path = action_handlres[a]()

        if ok:
            return True, a + path
    else:
        visited.remove(pos)
        return False, None


def CorrectPath(str1):
    ok, path = getPath(str1)
    # code goes here
    return path


# keep this function call here
print(CorrectPath("rd?u??dld?ddrr"))


'''
1. For the input "ddd?uru??ddd" your output was incorrect. The correct answer is dddrururrddd.
2. For the input "rd?u??dld?ddrr" your output was incorrect. The correct answer is rdrurrdldlddrr.
'''
















