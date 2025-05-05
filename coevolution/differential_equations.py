# implementation of https://drive.google.com/file/d/1ynZaaQ50zZGs588I27xy5al8orYr0eu6/view

import numpy as np
import matplotlib.pyplot as plt


class Simulation:
    def __init__(
        self,
        death_rate=0.01,  # δ (delta)
        birth_rate=0.02,  # μ (mu)
        reinfection_rate=0.005,  # ρ (roh)
        base_transmission_rate=0.5,  # β_0 (beta 0)
        recovery_rate=0.1,  # γ (gamma)
        waning_immunity=0.01,  # σ (sigma)
        modulation_factor=0.1,  # α (alpha)
        modulation_rate=1.0,  # r
        infected_population_carrying_capacity=1.0,  # K
        aging_rate=0.05,
    ):
        self.death_rate = death_rate
        self.birth_rate = birth_rate
        self.reinfection_rate = reinfection_rate
        self.base_transmission_rate = base_transmission_rate
        self.recovery_rate = recovery_rate
        self.waning_immunity = waning_immunity
        self.modulation_factor = modulation_factor
        self.modulation_rate = modulation_rate
        self.infected_population_carrying_capacity = (
            infected_population_carrying_capacity
        )

        # ADDED VARIABLES

        self.aging_rate = aging_rate

        # running variables
        self.transmission_rate = self.base_transmission_rate
        self.susceptible_population1 = 0.475
        self.susceptible_population2 = 0.475
        self.infected_population1 = 0.01
        self.infected_population2 = 0.05
        self.recovered_population = 0.0

        # static variables
        self.num_data_points = 6

    def get_data(self):
        return [
            self.susceptible_population1,
            self.susceptible_population2,
            self.infected_population1,
            self.infected_population2,
            self.recovered_population,
            self.transmission_rate,
        ]

    def step(self, delta_time):
        total_infected = self.infected_population1 + self.infected_population2
        self.transmission_rate = self.base_transmission_rate * (
            1
            + self.modulation_factor
            * self.modulation_rate
            * total_infected
            * (1 - total_infected / self.infected_population_carrying_capacity)
        )

        susceptible_population1_change = (
            self.birth_rate  # new life
            - self.aging_rate * self.susceptible_population1  # get older
            - self.transmission_rate * self.susceptible_population1 * (self.infected_population1 + self.infected_population2)
            + self.reinfection_rate * self.recovered_population
            - self.death_rate * self.susceptible_population1  # die
        )
        susceptible_population2_change = (
            self.aging_rate * self.susceptible_population1  # get older
            - self.transmission_rate * self.susceptible_population2 * (self.infected_population1 + self.infected_population2)
            - self.death_rate * self.susceptible_population2  # die
        )

        infected_population1_change = (
            self.transmission_rate * (self.susceptible_population1 + self.susceptible_population2) * self.infected_population1
            - self.recovery_rate * self.infected_population1
            - self.waning_immunity * self.infected_population1
            - self.death_rate * self.infected_population1
        )
        infected_population2_change = (
            self.transmission_rate * (self.susceptible_population1 + self.susceptible_population2) * self.infected_population2
            - self.recovery_rate * self.infected_population2
            - self.waning_immunity * self.infected_population2
            - self.death_rate * self.infected_population2
        )

        recovered_population_change = (
            self.recovery_rate * (self.infected_population1 + self.infected_population2)
            - self.reinfection_rate * self.recovered_population
            - self.death_rate * self.recovered_population
        )

        self.susceptible_population1 += susceptible_population1_change * delta_time
        self.susceptible_population2 += susceptible_population2_change * delta_time

        self.infected_population1 += infected_population1_change * delta_time
        self.infected_population2 += infected_population2_change * delta_time

        self.recovered_population += recovered_population_change * delta_time


def main():
    simulation = Simulation()
    num_datapoints = simulation.num_data_points
    iterations = 1000
    total_time = 100
    delta_time = total_time / iterations

    populations_list = np.zeros((iterations, num_datapoints))

    for i in range(iterations):
        populations_list[i] = np.array(simulation.get_data())
        simulation.step(delta_time)

    plt.figure(figsize=(10, 6))
    x = np.linspace(0, total_time, iterations)
    labels = [
        "susceptible1",
        "susceptible2",
        "infected1",
        "infected2",
        "recovered",
        "transmission_rate",
    ]
    for i in range(num_datapoints):
        plt.plot(x, populations_list[:, i], label=labels[i])

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
