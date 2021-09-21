from time import time


def time_execution(fn):
    def timing_wrapper(*args, **kwargs):
        start = time()
        res = fn(*args, **kwargs)
        finish = time()

        return res, (finish - start)
    return timing_wrapper