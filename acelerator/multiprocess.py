import threading
import multiprocessing
from acelerator.decorators import VicTimer as timer
import time


@timer  # not working the multiprocess part
def multiprocess_func(function, n, *args):  # TODO: not working at least in my computer
    print("Lets multiprocess!")

    processes = []

    for _ in range(n):
        p = multiprocessing.Process(target=function, args=(*args,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


@timer  # OK
def thread_func(function, n, *args):  # TODO: do the printing organized
    print("Lets thread!")

    threads = []

    for _ in range(n):
        t = threading.Thread(target=function, args=(*args,))
        t.start()
        threads.append(t)

    for process in threads:
        process.join()


if __name__ == '__main__':

    """dummy functions"""


    def do_something(seconds):
        print(f"Sleeping {seconds} second(s)...")
        time.sleep(seconds)
        return f"Done sleeping {seconds} second(s)"


    def print_arg(*args):
        time.sleep(1.5)
        for item in args:
            print(*item)


    @timer
    def simple_precess(args_list, n):
        print("simple process")
        for _ in range(n):
            print_arg(args_list)


    family = ["alma ", "annu ", "papa ", "mamma ", "mummo "]

    """using multiprocessing manually"""
    # import multiprocessing
    # processes = []
    #
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=(1.5,))
    #
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()
    #
    # finish = time.perf_counter()
    #
    # print(f"Finished in {round(finish - start, 2)} second(s)")

    """this will return as completed so 1, 2, 3, 4, 5"""
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     result = [executor.submit(do_something, sec) for sec in secs]
    #
    #     for f in concurrent.futures.as_completed(result):
    #         print(f.result())
    #
    # finish = time.perf_counter()
    # print(f"Finished in {round(finish - start, 2)} second(s)")

    """multiprocesing"""  # not working
    #
    # simple_precess(family, 10)
    #
    # multiprocess_func(print_arg, 10, family)

    # multiprocess_func(print_arg, 10, family)

    """adding @timer decorator"""  # works
    # timer.return_on = True
    #
    # simple_precess(family, 5)
    # thread_func(print_arg, 5, family)
    #
    # timer.return_on = False
    # thread_func(print_arg, 5, family)

    """adding a decorator"""


    def threading_decorator_function(original_function):
        def wrapper_threading(*args, **kwargs):

            threads = []
            n = 100
            for _ in range(n):
                t = threading.Thread(target=original_function, args=(*args,))
                t.start()
                threads.append(t)

            for process in threads:
                process.join()

            return original_function(*args, **kwargs)

        return wrapper_threading


    @threading_decorator_function(10)
    def simple_process(args_list, n):
        print("simple process")
        for _ in range(n):
            print_arg(args_list)


    simple_process(family, 5)
