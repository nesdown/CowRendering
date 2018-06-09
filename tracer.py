from KDTree import findIntersection
import vector_counts
import geometry_help


def build_plane(resolution, cam_pos, dir, distance):
    col_max = resolution[0] / 2
    row_max = resolution[1] / 2

    dir_vector = vector_counts.vec_mult(dir, distance)
    im_pos = vector_counts.vec_sum(cam_pos, dir_vector)

    koef = tuple(filter(lambda x: x != 0, dir_vector))[0]
    koef = dir_vector.index(koef)

    pix = [0, 0, 0]
    pix[koef] = im_pos[koef]

    [col_coord, row_coord] = [i for i, c in enumerate(dir_vector) if c == 0]

    plane = []
    row = row_max
    for i in range(resolution[1]):
        col = -col_max
        pix[row_coord] = row / row_max + cam_pos[row_coord]
        plane.append([])

        for j in range(resolution[0]):
            pix[col_coord] = col / col_max + cam_pos[col_coord]
            plane[i].append(tuple(pix))
            col += 1

        row -= 1

    return plane


def render(cam_pos, light_pos, im_pl, tree):
    image = [[colorify(cam_pos, pix, light_pos, tree) for pix in row] for row in im_pl]
    return image


def colorify(camera_pos, pix, light_pos, tree):
    px = 255
    light = 200

    ft, normal = find_intersections(camera_pos, pix, tree)

    if ft:
        color = vector_counts.vec_mult(vector_counts.vec_sum(normal, (1, 1, 1)), 0.5)
        px = vector_counts.vec_mult(color, 255)

    return px


def find_intersections(point1, point2, tree):
    distance, facet = findIntersection(point1, point2, tree)
    if distance == float('inf'):
        return None, None
    else:
        return facet['triangle'], facet['normal']
