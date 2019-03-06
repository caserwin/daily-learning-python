import numpy as np

events = np.array([[6, 5, 4, 3],
                   [5, 4, 3, 2],
                   [4, 3, 2, 1]])

print(events[:, ::-1].cumsum(1))

print(True + True)
print(True * True)