import time


def time_checker(func, num) -> tuple:
    start = time.time()
    return time.time() - start

print(time_checker(lambda trash: list(trash), range(1000000)))
