from joblib import Parallel, delayed

def square(n):
    return n * n

results = Parallel(n_jobs=4)(delayed(square)(i) for i in range(10))
print("Squares:", results)
