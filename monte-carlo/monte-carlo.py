from time import time
from math import exp, sqrt, log
from random import gauss, seed
import matplotlib.pyplot as plt
import pandas as pd


seed(0)
start_time = time()

# Parameters
S0 = 50         # initial value
K = 50          # strike price
years = 1.0     # maturity (years)
r = 0.05        # rate
sigma = 0.2    # volatility
N = 52 * 5      # number of time steps
dt = years / N  # length of time interval
num_sims = 10   # number of paths
plot = True     # enable plotting
csv_out = True  # write paths to csv

# Simulating num_sims paths with N time steps
paths = []
for i in range(num_sims):
    path = []
    for t in range(N + 1):
        if t == 0:
            path.append(S0)
        else:
            z = gauss(0.0, 1.0)
            St = path[t - 1] * exp((r - 0.5 * sigma ** 2) * dt
                        + sigma * sqrt(dt) * z)
            path.append(round(St, 4))

    paths.append(path)
    if plot:
        plt.plot(path)


opt_value = exp(-r * years) * sum([max(path[-1] - K, 0) for path in paths]) / num_sims

if csv_out:
    df = pd.DataFrame(list(zip(*paths))).add_prefix('sim')
    df.to_csv('./q2_out.csv', index=False)

ex_time = time() - start_time

if plot:
    plt.show()

print(f"European Option Value: {opt_value:.3f}")
print(f"Execution Time: {ex_time:.4f}")
