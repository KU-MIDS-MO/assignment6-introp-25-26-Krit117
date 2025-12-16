def random_unit_vectors(num_vectors, dim):
    import numpy as np
    M = np.random.randn(num_vectors, dim)
    for i in range (num_vectors):
        normalised_row= np.lingl.norm (M[i], ord=2)
        M[i]= M[i]/ normalised_row
        return np.array(M)
    
