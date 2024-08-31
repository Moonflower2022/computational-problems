import numpy as np

def iterate_unstable(balls):
  random = np.random.rand()*2 - 1
  if random**3 + 1 > 2*balls[0] / sum(balls) and random**3 + 1 <= 2:
    return 1
  elif random**3 + 1 <= 2*balls[0] / sum(balls) and random**3 + 1 >= 0:
    return 0
  
def iterate_stable(balls):
  if np.random.rand() > balls[0] / sum(balls):
    return 1
  else:
    return 0
  
'''
# timeline of proportions
data = []

for i in range(400):
  ball_plot = []
  balls = np.array([1, 1])
  for j in range(1000):
    ball_plot.append(balls[0] / sum(balls))
    balls[iterate_stable(balls)] += 10
  data.append(ball_plot.copy())

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
# plot the same data on both axes

for i in range(len(data)):
  ax1.plot(data[i])

plt.show()
'''

# histogram of ending proportions
data = []

for i in range(4000):
  balls = np.array([1, 1])
  for j in range(500):
    balls[iterate_stable(balls)] += 1
  data.append(balls[0] / sum(balls))

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots()
# plot the same data on both axes

plt.hist(data, bins=20, color='#37C5F9', edgecolor='black')

plt.xlabel('Ending proportion')
plt.ylabel('# of sims')

plt.show()