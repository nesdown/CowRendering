import vector_counts
from normalizer import normalize


def get_object_config(filename):
    configFile = open(filename, 'r')
    lines = [line.strip().split() for line in configFile]
    configFile.close()
    return lines


def get_vertices(model_res):
    verts = []

    for res in model_res:
        if not len(res):
            continue
        else:
            if res[0] == 'v':
                line = [float(value) for value in res[1:]]
                vertex = tuple(line)
                verts.append(vertex)

    print("Vertexes:")
    print(verts)
    return verts


def get_normals(model_res):
    norms = []

    for res in model_res:
        if not len(res):
            continue
        else:
            if res[0] == 'vn':
                line = [float(value) for value in res[1:]]
                norm = tuple(line)
                norms.append(norm)

    print("Normals:")
    print(norms)
    return norms


def get_facets(model_res):
    facets = []

    for res in model_res:
        if not len(res):
            continue
        else:
            if res[0] == 'f':
                line = [int(value.split('/')[0]) for value in res[1:]]
                facet = tuple(line)
                facets.append(facet)

    print("Facets:")
    print(facets)
    return facets


def get_final_facets(vertices, facets):
    final_facets = []

    for facet in facets:
        prepared = [vertices[index - 1] for index in facet]
        final_facets.append(prepared)

    return final_facets
