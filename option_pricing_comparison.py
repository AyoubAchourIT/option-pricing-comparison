import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def black_scholes_call(S0, K, r, sigma, T):
    """Price a European call option with the Black-Scholes formula."""
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def monte_carlo_call(S0, K, r, sigma, T, n_simulations=100_000, seed=42):
    """Estimate a European call option price with Monte Carlo simulation."""
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(n_simulations)
    ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0.0)
    return np.exp(-r * T) * np.mean(payoffs)


def binomial_call(S0, K, r, sigma, T, N=100):
    """Price a European call option with a CRR binomial tree."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    discount = np.exp(-r * dt)

    stock_prices = np.array([S0 * (u ** j) * (d ** (N - j)) for j in range(N + 1)])
    option_values = np.maximum(stock_prices - K, 0.0)

    for step in range(N, 0, -1):
        option_values = discount * (
            p * option_values[1 : step + 1] + (1 - p) * option_values[0:step]
        )

    return option_values[0]


def main():
    S0 = 100
    K = 100
    r = 0.03
    sigma = 0.20
    T = 1

    bs_price = black_scholes_call(S0, K, r, sigma, T)
    mc_price = monte_carlo_call(S0, K, r, sigma, T, n_simulations=100_000)
    bin_price = binomial_call(S0, K, r, sigma, T, N=100)

    print("European Call Option Pricing Comparison")
    print("-" * 40)
    print(f"Black-Scholes price : {bs_price:.6f}")
    print(f"Monte Carlo price   : {mc_price:.6f}")
    print(f"Binomial tree price : {bin_price:.6f}")
    print()
    print("Differences")
    print("-" * 40)
    print(f"|Monte Carlo - Black-Scholes| = {abs(mc_price - bs_price):.6f}")
    print(f"|Binomial - Black-Scholes|    = {abs(bin_price - bs_price):.6f}")
    print(f"|Monte Carlo - Binomial|      = {abs(mc_price - bin_price):.6f}")

    steps = np.arange(5, 501)
    binomial_prices = [binomial_call(S0, K, r, sigma, T, N=n) for n in steps]

    plt.figure(figsize=(10, 6))
    plt.plot(steps, binomial_prices, label="Binomial tree price", color="tab:blue")
    plt.axhline(
        y=bs_price,
        color="tab:red",
        linestyle="--",
        label="Black-Scholes price",
    )
    plt.title("Convergence of Binomial Tree Price to Black-Scholes Price")
    plt.xlabel("Number of binomial steps (N)")
    plt.ylabel("Option price")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("binomial_convergence.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
