def get_statistics(input_list):
    input_list = sorted(input_list)
    sum = 0.
    freq={}
    
    for i in input_list:
        sum += i
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1

    u = sum/len(input_list)
    mod  = max(freq, key=freq.get)
    if len(input_list)%2==0:
        median = (input_list[len(input_list)//2] + input_list[(len(input_list)-1)//2])/2.0
    if len(input_list)%2!=0:
        median=input_list[(len(input_list)-1) //2]
    
    var_dem = len(input_list)-1
    var_nem = 0.
    for i in input_list:
        var_nem += (i-u)**2
    
    var = var_nem / var_dem
    std= (var)**0.5
    
    SE=std/(len(input_list))**0.5
    conf_interval_max = u + (1.96*SE)
    conf_interval_min = u - (1.96*SE)

    return {
        "mean": u,
        "median": median,
        "mode": mod,
        "sample_variance": var,
        "sample_standard_deviation": std,
        "mean_confidence_interval": [conf_interval_min, conf_interval_max],
    }