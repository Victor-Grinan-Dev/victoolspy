from functools import wraps
import threading
import logging
import time


# example
def decorator1(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result

    return wrapper


def decorator2(original_function):
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result

    return wrapper


class VicTimer(object):
    execute_on = True
    return_on = False

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):

        if self.execute_on:
            self.return_on = False
        elif self.return_on:
            self.execute_on = False

        t1 = time.time()
        result = self.original_function(*args, **kwargs)
        t2 = time.time() - t1

        if self.execute_on:
            print(f"original {self.original_function.__name__} executed execute in {t2:.2f} sec(s)")
        else:
            return result  # self.original_function(*args, **kwargs)

    @staticmethod
    def start_timer():
        return time.perf_counter()

    @staticmethod
    def stop_timer(start):
        finish = time.perf_counter()
        print(f"Finished in {round(finish - start, 2)} second(s)")


class VicLogger(object):
    print_on = False

    def __init__(self, original_function):
        logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        logging.info(
            f"{self.original_function.__name__} executed with args: {args}, and kwargs: {kwargs} ")
        return self.original_function(*args, **kwargs)


class VicTimerLog(object):
    print_on = False

    def __init__(self, original_function):
        logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        t1 = time.time()
        result = self.original_function(*args, **kwargs)
        logging.info(f"{self.original_function.__name__} executed with args: {args}, and kwargs: {kwargs} ")
        t2 = time.time() - t1
        if self.print_on:
            print(f"original {self.original_function.__name__} executed execute in {t2:.2f} sec(s)")
        return self.original_function(*args, **kwargs)


class VicThread(object):
    print_on = False
    loops = 1

    def __init__(self, original_function):
        self.original_function = original_function

        self.start = VicTimer.start_timer()

    def __call__(self, *args, **kwargs):
        threads = []

        for _ in range(self.loops):
            try:
                t = threading.Thread(target=self.original_function, args=(*args,))
                t.start()
                threads.append(t)

            except RuntimeError:
                pass
        for thread in threads:
            thread.join()

        VicTimer.stop_timer(self.start)

        # return self.original_function(*args, **kwargs)


if __name__ == '__main__':
    # LEARNING & TESTING
    #
    # # decorators
    # def decorator_function(original_function):
    #     def wrapper_function(*args, **kwargs):
    #         print(f"wrapper function executed before {original_function.__name__}")
    #         return original_function(*args, **kwargs)
    #
    #     return wrapper_function
    #
    #
    # @decorator_function
    # def display_info(name, age):
    #     print(f"display function run with arguments {name} and {age}")
    #
    #
    # # display_info('john', 30)
    #
    # # implementing in class example
    # class Decorator_class(object):
    #     def __init__(self, original_function):
    #         self.original_function = original_function
    #
    #     def __call__(self, *args, **kwargs):
    #         print(f"wrapper class executed before {self.original_function.__name__}")
    #         return self.original_function(*args, **kwargs)
    #
    #
    # @Decorator_class
    # def display_info(name, age):
    #     print(f"display function run with arguments {name} and {age}")
    #
    #
    # # display_info('victor', 37)
    #
    # # practical example
    # def my_logger(original_function):
    #     import logging
    #     logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)
    #
    #     @wraps(original_function)
    #     def wrapper_function(*args, **kwargs):
    #         logging.info(
    #             f"{original_function.__name__} executed with args: {args}, and kwargs: {kwargs} ")
    #         return original_function(*args, **kwargs)
    #
    #     return wrapper_function
    #
    #
    # def my_timer(original_function):
    #     import time
    #
    #     @wraps(original_function)
    #     def wrapper_function(*args, **kwargs):
    #         t1 = time.time()
    #         result = original_function(*args, **kwargs)
    #         t2 = time.time() - t1
    #         print(f"original {original_function.__name__} executed execute in {t2:.2f} sec(s)")
    #         return original_function(*args, **kwargs)
    #
    #     return wrapper_function
    #
    #
    # @my_timer
    # @my_logger
    # def display_info(arg1, arg2):
    #     print(f"display function run with arguments {arg1} and {arg2}")
    #
    #
    # # display_info("annu", "victor")
    #
    # # implementing in class example
    # class Timertool(object):
    #
    #     def __init__(self, original_function):
    #         self.original_function = original_function
    #
    #     def __call__(self, *args, **kwargs):
    #         t1 = time.time()
    #         result = self.original_function(*args, **kwargs)
    #         t2 = time.time() - t1
    #         print(f"original {self.original_function.__name__} executed execute in {t2:.2f} sec(s)")
    #         return self.original_function(*args, **kwargs)
    #
    #
    # @Timertool
    # def display_info(arg1, arg2):
    #     print(f"display function run with arguments {arg1} and {arg2}")
    #
    #
    # display_info("annu", "victor")

    # @VicTimerLog
    # def display_info(arg1, arg2):
    #     print(f"display function run with arguments {arg1} and {arg2}")

    def display_info(arg1, arg2):
        time.sleep(1)
        print(f"{display_info.__name__} run with arguments {arg1} and {arg2}")


    decorated_function = VicThread(display_info)

    decorated_function.loops = 950

    decorated_function("annu", "victor")
