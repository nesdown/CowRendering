from vector_counts import vector, vec_norm, vec_sum

eps = 1e-8


def centroid(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]

    x_cen = (x1 + x2 + x3) / 3
    y_cen = (y1 + y2 + y3) / 3
    z_cen = (z1 + z2 + z3) / 3

    return x_cen, y_cen, z_cen


def cross_vector(vec1, vec2):
    x = vec1[1] * vec2[2] - vec1[2] * vec2[1]
    y = vec1[2] * vec2[0] - vec1[0] * vec2[2]
    z = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    return x, y, z


def dot_vector(vec1, vec2):
    x = vec1[0] * vec2[0]
    y = vec1[1] * vec2[1]
    z = vec1[2] * vec2[2]
    return x + y + z


def intersection(point1, point2, facet):
    origin = point1
    direction = vector(point1, point2)

    edge1 = vector(facet[0], facet[1])
    edge2 = vector(facet[0], facet[2])

    pvec = cross_vector(direction, edge2)
    det = dot_vector(edge1, pvec)

    if eps > det > -eps:
        return float('inf')

    tvec = vector(facet[0], origin)
    u = dot_vector(tvec, pvec) / det

    if u < 0 or u > 1:
        return float('inf')

    qvec = cross_vector(tvec, edge1)
    v = dot_vector(direction, qvec) / det

    if v < 0 or u + v > 1:
        return float('inf')


def rb_intersection(point1, point2, box):
    x0, y0, z0 = box[0]
    x1, y1, z1 = box[1]

    m, n, p = vec_norm(vector(point1, point2))
    x, y, z = point1

    closest, furthest = -float('inf'), float('inf')
    if m == 0:
        if x > x1 or x < x0:
            return float('inf')
    else:
        closest = (x0 - x) / m
        furthest = (x1 - x) / m
        if closest > furthest: furthest, closest = closest, furthest

    if n == 0:
        if y > y1 or y < y0:
            return float('inf')
    else:
        T1y = (y0 - y) / n
        T2y = (y1 - y) / n

        if T1y > T2y: T2y, T1y = T1y, T2y

        if T1y > closest: closest = T1y
        if T2y < furthest: furthest = T2y

    if closest > furthest or furthest < 0:
        return float('inf')

    if p == 0:
        if z > z1 or z < z0:
            return float('inf')
    else:
        T1z = (z0 - z) / p
        T2z = (z1 - z) / p

        if T1z > T2z: T2z, T1z = T1z, T2z

        if T1z > closest: closest = T1z
        if T2z < furthest: furthest = T2z

    if closest > furthest or furthest == 0:
        return float('inf')

    return closest


def avg_normal(normals):
    norm1, norm2, norm3 = normals
    normal = vec_sum(norm1, norm2)
    normal = vec_sum(normal, norm3)
    return vec_norm(normal)
