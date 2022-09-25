import random
import numpy as np

class Centroid:
    def __init__(self, pos):
        self.pos = pos
        self.nearest_points = set()

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

def average_position(centroid,data):
    no_features = len(data[0])
    no_close_points = len(centroid.nearest_points)
    average_in_dims = [0] * no_features
    for i in range(no_features):
        for id in centroid.nearest_points:

            average_in_dims[i] += data[id][i]
    return [dim/no_close_points for dim in average_in_dims]




class k_means:

    def __init__(self, no_clusters, random_state, iters, distance) -> None:
        distances_dict = {"manhattan": manhattan_distance,"ecludiean":ecludiean_distance}
        self.no_clusters = no_clusters
        self.iters = iters
        self.random_state = random_state
        self.distance = distances_dict[distance]
        self.kcentroids=[]
        





    def fit(self, data):
        if len(self.kcentroids) == 0:
            init_centroid = random.sample(list(data), self.no_clusters)        
            self.kcentroids = [Centroid(pos) for pos in init_centroid]

        for iter in range(self.iters):
            for id, features in enumerate(data):
                lowest_distance_to_centroid = float("inf")
                nearest_centroid = Centroid(None)
                for centroid in self.kcentroids:

                    features_centroid_distance = manhattan_distance(
                        features, centroid.pos)
                    if features_centroid_distance < lowest_distance_to_centroid:
                        lowest_distance_to_centroid=features_centroid_distance 
                        nearest_centroid = centroid
                nearest_centroid.nearest_points.add(id)
    

            for i,centroid in enumerate(self.kcentroids):
                centroid.pos = average_position(centroid,data)
                if iter != self.iters:
                    centroid.nearest_points.clear()
            print(f"Finished {iter+1} iterations")
        self.kcentroids=self.kcentroids
        


    def get_centroids(self):

            return[ tuple(centroid.pos) for centroid in self.kcentroids]