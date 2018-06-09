import obj_parser
import tracer
import KDTree
import out_former
from time import time

start = time()
facets = obj_parser.get_object_config(input("Enter the model name: "), True)

cameraPos = (0.25, -1, 0.3)
direction = (0, 1, 0)
lightPos = (10, -10, 10)
size = (1024, 1024)
distance = 1

imagePlane = tracer.build_plane(size, cameraPos, direction, distance)
tree = KDTree.buildTree(facets)

image = tracer.render(cameraPos, lightPos, imagePlane, tree)
print(time() - start)

out_former.make_bmp(image, size, 'cow.bmp')
