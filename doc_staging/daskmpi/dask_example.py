import time
from dask import delayed


def time_usage(func):
    def wrapper(*args, **kwargs):
        beg_ts = time.time()
        retval = func(*args, **kwargs)
        end_ts = time.time()
        print("elapsed time: %f" % (end_ts - beg_ts))
        return retval
    return wrapper


def inc(x):
    time.sleep(1)
    return x + 1


def main():
    data = list(range(1, 9))
       
    # Sequential code
    @time_usage
    def _():
        results = []
        for x in data:
            y = inc(x)
            results.append(y)
        total = sum(results)
        print("%s"%total)
    _()
    
    # parallel code
    @time_usage
    def _():
        results = []
        for x in data:
            y = delayed(inc)(x)
            results.append(y)
        total = delayed(sum)(results)
        result = total.compute()
        print("%s\n"%result)
    _()


if __name__ == "__main__":
    main()

