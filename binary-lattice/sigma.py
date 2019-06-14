import numpy as np

__author__ = "Andrew Vaillancourt"


def bin_opt_tree(S0, K, T, r, sigma, N, show_tree=False):
    dt = T/N
    u = np.exp(sigma*np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt)-d)/(u-d)

    price_tree = np.zeros([N+1, N+1])

    for i in range(N+1):
        for j in range(i+1):
            price_tree[j, i] = S0*(d**j)*(u**(i-j))

    option = np.zeros([N+1, N+1])
    option[:, N] = np.maximum(np.zeros(N+1), price_tree[:, N]-K)

    for i in np.arange(N-1, -1, -1):
        for j in np.arange(0, i+1):
            option[j, i] = np.exp(-r*dt)*(p*option[j, i+1]+(1-p)*option[j+1, i+1])

    if show_tree:
        return [option[0,0], price_tree, option]
    else:
        return option[0, 0]


if __name__ == "__main__":

    S0 = 50         # initial asset price
    K = 50          # strike price
    T = 1           # expiration date (years)
    r = 0.05        # interest rate
    sigma = 0.05    # volatility
    N = 512         # tree steps

    ret_tree = True
    print_tree = False

    for i in range(0, 10):
        vals = bin_opt_tree(S0, K, T, r, sigma, N, ret_tree)
        np.set_printoptions(precision=3)
        print(f"{sigma}, {vals[0]:.4f}")

        if ret_tree and print_tree:
            print("\nTree")
            print("===========================================")
            print(vals[1])
            print("===========================================")

        sigma = round(sigma + 0.05, 2)

