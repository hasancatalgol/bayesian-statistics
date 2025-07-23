import arviz as az
import matplotlib.pyplot as plt

def analyze_trace(trace):
    az.plot_trace(trace)
    plt.tight_layout()
    plt.show()

    az.plot_posterior(trace)
    plt.tight_layout()
    plt.show()

    print(az.summary(trace, hdi_prob=0.95))
