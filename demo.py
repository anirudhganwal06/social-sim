import numpy as np

# arr = [1, 2, 3, 4, {'abc': 'def'}]
# np.save('network1.npy', arr, allow_pickle = True)

arr = np.load('network1.npy', allow_pickle = True)
print(arr)