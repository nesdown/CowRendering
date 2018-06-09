import vector_counts


def normalize(verts):
    max_vertex = max(verts, key=lambda v: vector_counts.vec_len(v))
    max_len = vector_counts.vec_len(max_vertex)

    return list(map(
        lambda v: (v[0] / max_len, v[1] / max_len, v[2] / max_len), verts
    ))
