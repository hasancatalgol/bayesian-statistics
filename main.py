import pymc as pm
import pandas as pd
import arviz as az
import numpy as np

# Set PyMC to use Numba for performance
import pytensor
pytensor.config.mode = "NUMBA"

# Load dataset
df = pd.read_csv("data/concrete_cleaned.csv")
print(df.columns.tolist())

# Normalize input features
X = df.drop(columns=["strength"])
X = (X - X.mean()) / X.std()
y = df["strength"].values
x_data = X.values
n_features = x_data.shape[1]

with pm.Model() as model:
    # Priors
    intercept = pm.Normal("intercept", mu=0, sigma=10)
    betas = pm.Normal("betas", mu=0, sigma=1, shape=n_features)
    sigma = pm.HalfNormal("sigma", sigma=5)

    # Linear model
    mu = intercept + pm.math.dot(x_data, betas)

    # Likelihood
    y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

    # Use ADVI (fast, works without g++)
    approx = pm.fit(n=5000, method="advi")
    trace = approx.sample(1000)

# Posterior summary
az.plot_trace(trace)
az.plot_posterior(trace)
print(az.summary(trace, hdi_prob=0.95))
