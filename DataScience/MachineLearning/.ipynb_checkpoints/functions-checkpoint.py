import numpy as np
import pandas as pd


random_generator = np.random.default_rng()


def generate_data(n_features, n_values):
    features = random_generator.random((n_features, n_values))
    weights = random_generator.random((1, n_values))[0]
    targets = np.random.choice([0, 1], n_features)
    data = pd.DataFrame(features, columns=["x0", "x1", "x2"])
    data["targets"] = targets
    return data, weights