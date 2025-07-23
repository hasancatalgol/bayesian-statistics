import pymc as pm

def run_inference(model, method="mcmc"):
    with model:
        if method == "advi":
            approx = pm.fit(n=5000, method="advi")
            return approx.sample(1000)
        else:
            return pm.sample(2000, tune=1000, target_accept=0.9, return_inferencedata=True)
        
# Markov chain Monte Carlo (MCMC)
