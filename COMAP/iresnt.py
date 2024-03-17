import numpy as np
import matplotlib.pyplot as plt

# time in days
# length in meters
# temperature in F

optimal_temp = (50, 75)
temp_range = 5.6
temperatures = np.array([
    31.17,  # January
    33.67,  # February
    44.08,  # March
    50.65,  # April
    61.90,  # May
    70.79,  # June
    76.41,  # July
    74.57,  # August
    68.02,  # September
    55.24,  # October
    40.87,  # November
    33.08   # December
])
reproduction_rate = 200
reproduction_power = 200
reproduction_radius = 50
size = 10000


def temperature_coefficient(temp, minimum, maximum, span):
    coef = np.ones_like(temp)
    mask = (minimum <= temp) & (temp <= maximum)
    coef[~mask] = np.maximum((temp[~mask] - minimum) / span + 1, 0)
    coef[temp > maximum] = np.maximum((maximum - temp[temp > maximum]) / span + 1, 0)
    return coef

def proximity_multiplier(pos, plants, radius):
    if plants.shape[0] == 0:
        return 1
    distances = np.linalg.norm(plants - pos, axis=1)
    distances = distances[distances <= radius] / radius
    distances = distances[distances != 0]  # exclude current seed
    return 1 if distances.shape[0] == 0 else np.min(distances)

def reproduce(pos, month, temps, power, radius, boundary, first, plants, proximity_radius):
    num_points = power * (1 if first else temperature_coefficient(temps[month], optimal_temp[0], optimal_temp[1], temp_range))
    proximity = proximity_multiplier(pos, plants, proximity_radius)
    num_points = int(num_points * proximity)
    theta = 2 * np.pi * np.random.random(num_points)
    point_radius = np.random.random(num_points) * radius
    points = np.array([np.cos(theta), np.sin(theta)]).T * point_radius[:, None] + pos
    points = points[(points < boundary).all(axis=1) & (points > 0).all(axis=1)]
    return points

months = 7
proximity_radius = 0.1524
starting_seed = np.array([size] * 2)/2

pop_loc = np.vstack([starting_seed, *reproduce(starting_seed, 0, temperatures, reproduction_power, reproduction_radius, size, True, np.array([]), proximity_radius)])
gen = 1
for day in range(int(months * 30)):
    if day > gen * reproduction_rate and int(reproduction_power * temperature_coefficient(temperatures[int(day/30.437)], optimal_temp[0], optimal_temp[1], temp_range)) != 0:
        new_seeds = [reproduce(seed, int(day/30.437), temperatures, reproduction_power, reproduction_radius, size, False, pop_loc, proximity_radius) for seed in pop_loc]
        pop_loc = np.concatenate([pop_loc, *new_seeds])
        gen += 1
    # Remove dead plants based on death rate
    death_rates = 1 - np.array([proximity_multiplier(seed, pop_loc, proximity_radius) for seed in pop_loc])
    death_indices = np.where(death_rates > 0)[0]
    pop_loc = np.delete(pop_loc, death_indices, axis=0)
fig, ax = plt.subplots()
ax.set(xlim=(0, size), ylim=(0, size))
plt.scatter(pop_loc[:, 0], pop_loc[:, 1], s=1)
plt.title(f'Population: {len(pop_loc)}, Months: {months}')
plt.show()