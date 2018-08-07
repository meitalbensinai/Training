import numpy as np

X = np.random.randn(4, 2) # random normals in 4x2 array
print(X)

# For each column find the row index of the minimum value
print(np.amin(X, axis=0))


# Write a function standardize(X) that return an array whose columns are centered and scaled (by std-dev).
def standardize(vec):
    mean_ = np.mean(vec, axis=0)
    scale_ = np.std(vec, axis=0)
    scale_[scale_ == 0.0] = 1.0

    # center the data
    vec -= mean_

    # scale the data
    vec /= scale_
    return vec


print(standardize(X))
