import numpy as np
a = np.arange(1,64,4)
a = a.reshape(4,4)
print('Original array is:')
print(a)
print('\n')
print('Modified array is:')
for x in np.nditer(a):
   print(x)

