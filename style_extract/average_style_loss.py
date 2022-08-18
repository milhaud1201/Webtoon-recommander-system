import numpy as np

def avgList(result, label_arr):

    labels = np.array(label_arr)
    avg_list = [None] * len(np.unique(labels))
    
    for label in np.unique(labels):
        temp_avg = []
        for idx in range(len(result)):
            if label_arr[idx] == label:
                temp_avg.append(result[idx])
        avg_list[label] = np.mean(temp_avg, axis=0)

    return avg_list
