import numpy as np
import matplotlib.pyplot as plt
# gamma >= 0
# beta >= 0
# 0 <= x <= 1


class Sim:
    def __init__(self, time_steps, Y, C, U, i, I, P, P_e, F, gamma, beta, M_s, mu, z, LF, G, T):
        self.Y, self.C, self.U, self.i, self.I, self.P, self.P_e, self.F, self.gamma, self.beta, self.M_s, self.mu, self.z, self.LF, self.G, self.T = (
            Y, C, U, i, I, P, P_e, F, gamma, beta, M_s, mu, z, LF, G, T)
        self.iterations = 0
        self.previous = []
        self.previous_averaging = []
        self.time_steps = time_steps

    def avg(self, var):
        return np.mean([item[var] for item in self.previous_averaging])

    def get_last(self, var):
        return self.previous[-1][var]

    def update_previous(self, new):
        self.previous.append(new)
        self.previous = self.previous[-4:]

    def update_previous_averaging(self, new):
        self.previous_averaging.append(new)
        self.previous_averaging = self.previous_averaging[-4:]

    def iterate(self):
        self.update_previous_averaging({
            "U": max(1 - self.Y/self.LF, 0),
            "F": self.z / self.U,
            "P_e": self.P,
            "P": (1 + self.mu) * self.P_e * self.F
        })
        self.update_previous({
            "Y": self.Y,
            "C": self.C,
            "U": self.U,
            "i": self.i,
            "I": self.I,
            "P": self.P,
            "P_e": self.P_e,
            "F": self.F
        })
        if self.iterations >= self.time_steps:
            self.U = self.avg("U")
            self.P = self.avg("P")
            self.P_e = self.avg("P_e")
            self.F = self.avg("F")
        self.Y = self.previous[-1]["C"] + self.previous[-1]["I"] + self.G
        self.C = self.gamma * max(self.previous[-1]["Y"] - self.T, 0)
        self.i = self.beta * self.previous[-1]["Y"] * self.previous[-1]["P"] / self.M_s
        self.I = self.beta * self.previous[-1]["Y"] / (1 + self.previous[-1]["i"])
        self.iterations += 1

    def __str__(self):
        changed_vars = {
            'Y': self.Y, 'C': self.C, 'U': self.U, 'i': self.i, 'I': self.I,
            'P': self.P, 'P_e': self.P_e, 'F': self.F
        }

        changed_vars_str = ', '.join(
            f'{var}={value:.3f}' for var, value in changed_vars.items())
        return f'Sim(iterations={self.iterations}, {changed_vars_str})'


model = Sim(time_steps=4, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.6, gamma=0.3, beta=0.03, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=1, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.1, gamma=0.5, beta=0.7, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=15, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.1, gamma=0.5, beta=0.7, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=7, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.1, gamma=0.8, beta=0.3, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=7, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.1, gamma=0.6, beta=0.5, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=4, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, P_e=1, F=0.1, gamma=0.6, beta=0.5, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)
#model = Sim(time_steps=4, Y=1, C=0.75, U=0.05, i=0.04, I=0.2, P=1, how to play gimkit plants vs zombiesP_e=1, F=0.6, gamma=0.4, beta=0.8, M_s=0.8, mu=0.4, z=0.35, LF=1.2, G=0.2, T=0.25)


sims = 60

# Lists to store values for plotting
iterations = []
Y_values = []
C_values = []
U_values = []
i_values = []
I_values = []
P_values = []
P_e_values = []
F_values = []

# Perform simulations and collect values
for _ in range(sims + 1):
    iterations.append(model.iterations)
    Y_values.append(model.Y)
    C_values.append(model.C)
    U_values.append(model.U)
    i_values.append(model.i)
    I_values.append(model.I)
    P_values.append(model.P)
    P_e_values.append(model.P_e)
    F_values.append(model.F)
    model.iterate()

# Plot the values
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig.suptitle(f"tau: {model.time_steps}, gamma: {model.gamma}, beta: {model.beta}, {sims} iterations", y=0.95)

# Plot for variables that stay between 1 and 0 (U, C, i, I)
ax1.plot(iterations, U_values, label='U')
ax1.plot(iterations, C_values, label='C')
ax1.plot(iterations, I_values, label='I')
ax1.set_ylabel('Values')
ax1.set_yticks(np.arange(0, 1.1, 0.2))  # Set y-ticks from 0 to 1 with a step of 0.2
ax1.legend()

# Plot for the rest of the variables
ax2.plot(iterations, i_values, label='i')
ax2.plot(iterations, Y_values, label='Y')
ax2.plot(iterations, P_values, label='P')
ax2.plot(iterations, P_e_values, label='P_e')
ax2.plot(iterations, F_values, label='F')
ax2.set_xlabel('Iterations')
ax2.set_ylabel('Values')
ax2.legend()

plt.show()
