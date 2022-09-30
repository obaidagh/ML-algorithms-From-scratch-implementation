
def average_position(centroid,data):

    no_features = len(data[0])
    no_close_points = len(centroid.nearest_points)
    average_in_dims = [0] * no_features
    
    for i in range(no_features):
        for id in centroid.nearest_points:

            average_in_dims[i] += data[id][i]
    
    return [dim/no_close_points for dim in average_in_dims]
