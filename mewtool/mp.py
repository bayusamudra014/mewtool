import multiprocessing as mp


def iterate_parallel(func, iterable, n_jobs=mp.cpu_count()):
    with mp.Pool(n_jobs) as pool:
        return pool.map(func, iterable)
