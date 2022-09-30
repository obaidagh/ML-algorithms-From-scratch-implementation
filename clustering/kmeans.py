import random
import numpy as np

from helpers.distances import manhattan_distance,ecludiean_distance
from helpers.postions import average_position
from centroid import Centroid







class Kmeans:

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
                #if iter != self.iters:
                #    centroid.nearest_points.clear()
                centroid.nearest_points.clear()
            print(f"Finished {iter+1} iterations")
        self.kcentroids=self.kcentroids
        


    def get_centroids(self):

            return[ tuple(centroid.pos) for centroid in self.kcentroids]