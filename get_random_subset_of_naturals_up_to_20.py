def get_random_subset_of_naturals_up_to_20():
    import numpy as np
    subset = []
    for i in range (1,21):
        if np.random.rand()>0.5:
            subset.append(i)
    return np.array(subset)