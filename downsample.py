from scipy import signal
import json
import numpy as np

max_lines = 5000000
resample_factor = 25


def downsample(file_path, downsample_rate):

    # Get data
    data = np.loadtxt(file_path, skiprows=1, delimiter=",", max_rows=max_lines)

    # Switch to numpy array 
    data_array = data.view()
    data_array = data_array.transpose()
    data_array = np.nan_to_num(data_array)

    # Resample data
    data_resampled = signal.resample(data_array[1], int(max_lines/resample_factor))

    with open(file_path + '-downsampled.json', 'w') as f:
        json.dump({'data':data_resampled.tolist()}, f)

    return data_resampled
