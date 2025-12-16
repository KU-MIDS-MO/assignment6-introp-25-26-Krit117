def estimate_pi(num_samples):
    import numpy as np
    x = np.random.rand(num_samples)
    y = np.random.rand(num_samples)
    inside_circle = (x**2 + y**2) <= 1
    pi_estimate = 4 * np.sum(inside_circle) / num_samples
    return pi_estimate
