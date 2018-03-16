f = open('inside_poly1.txt')
def input():
    return f.readline()


import sys

from math import acos, sqrt


def pt2normvec(pt0, pt1):
    x0, y0 = pt0
    x1, y1 = pt1

    vec1 = [x1 - x0, y1 - y0]
    v1_norm = sqrt(vec1[0] * vec1[0] + vec1[1] * vec1[1])
    vec1[0] /= v1_norm
    vec1[1] /= v1_norm

    return vec1


def angle(pt1, pt0, pt2):
    vec1 = pt2normvec(pt0, pt1)
    vec2 = pt2normvec(pt0, pt2)

    cos_phi = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    phi = acos(cos_phi)

    # evaluate cross product k sign
    k = vec1[0] * vec2[1] - vec1[1] * vec2[0]

    if k > 0:
        return -phi
    else:
        return phi


n = int(input())
pts = []
for i in range(n):
    x, y = [float(x) for x in input().strip().split(' ')]
    pts.append((x, y))

pt0 = [float(x) for x in input().strip().split(' ')]

angle_sum = angle(pts[n - 1], pt0, pts[0])
for i in range(1, n):
    phi = angle(pts[i - 1], pt0, pts[i])
    angle_sum += phi

print('Inside' if angle_sum > 1.0 else 'Outside')
