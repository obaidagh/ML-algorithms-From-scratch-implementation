import random
import math


def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.
    knn = find_k_nearest_neighbors(examples, features, k)
    vote = 0
    for i, dp in enumerate(knn):

        vote += examples[dp][label_key]

    vote = vote/(len(knn))
    
    if vote == 0.5:
        predict_label(examples, features, k+1, label_key="is_intrusive")
    if vote > 0.5:
        return 1
    else:
        return 0


def find_k_nearest_neighbors(examples, features, k):
    # Write your code here.
    distance = {}
    for dp in examples.keys():
        ecludiean = 0
        for i in range(len(features)):
            ecludiean += (features[i] - examples[dp]["features"][i])**2

        ecludiean = math.sqrt(ecludiean)
        distance[dp] = ecludiean

    return sorted(distance, key=distance.get)[:k]

