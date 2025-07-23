import pymc as pm

def build_model(x_data, y, n_features):
    with pm.Model() as model:
        intercept = pm.Normal("intercept", mu=0, sigma=10)
        betas = pm.Normal("betas", mu=0, sigma=1, shape=n_features)
        sigma = pm.HalfNormal("sigma", sigma=5)
        mu = intercept + pm.math.dot(x_data, betas)
        y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)
    return model
    
