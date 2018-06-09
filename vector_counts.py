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
