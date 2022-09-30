import numpy as np

def ecludiean_distance(features,other_features):

    point1 = np.array(features)
    point2 = np.array(other_features)
    

    temp = point1 - point2

    sum_sq = np.dot(temp.T, temp)

    return list(np.sqrt(sum_sq))

def manhattan_distance(features, other_features):
    absolute_differences = []
    for i in range(len(features)):
        absolute_differences.append(abs(features[i]-other_features[i]))
    return sum(absolute_differences)