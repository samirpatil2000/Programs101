

import numpy as np
def cosine(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2) / (np.sqrt(np.sum(v1)) * np.sqrt(np.sum(v2)))

def nearestPoint(space,point):
    return min(space, key=lambda p: cosine(point, p))





point=[2,2]
space=[[4,4],[1,1]]


point=[2,2]
space=[[3,3],[1,1]]
print(nearestPoint(space,point))