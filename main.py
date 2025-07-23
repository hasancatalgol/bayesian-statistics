import pytensor
pytensor.config.mode = "NUMBA"

from data_loader import load_data
from preprocessing import normalize_features
from model_definition import build_model
from inference import run_inference
from analysis import analyze_trace

def main():
    # Load and preprocess
    X, y = load_data()
    X_norm = normalize_features(X)
    x_data = X_norm.values
    y_data = y.values
    n_features = x_data.shape[1]

    # Build model
    model = build_model(x_data, y_data, n_features)

    # Run inference (default: MCMC)
    trace = run_inference(model, method="mcmc")

    # Analyze
    analyze_trace(trace)

if __name__ == "__main__":
    main()
