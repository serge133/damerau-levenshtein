import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

# Y = np.random.rand(100, 10)

A = [[0.0,0.1,0.2,0.3], [0.35, 0.4,0.5,0.6], [0.7,0.8,0.9, 1.0]]

plt.pcolor(A)
plt.title('Graph')
plt.ylabel("Search Results")
plt.xlabel('Participants')
# plt.text('Test', 'Test Y', )

plt.show()

