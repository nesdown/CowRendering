import math as m


def vector(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    vec = (x2 - x1, y2 - y1, z2 - z1)

    return vec


def vec_len(vec):
    x, y, z = vec
    return m.sqrt(x ** 2 + y ** 2 + z ** 2)


def vec_norm(vec):
    len = vec_len(vec)
    x, y, z = vec

    return x / len, y / len, z / len


def vec_sum(vector1, vector2):
    x = vector1[0] + vector2[0]
    y = vector1[1] + vector2[1]
    z = vector1[2] + vector2[2]
    return x, y, z


def vec_mult(vec, num):
    return tuple(map(lambda v: v * num, vec))
