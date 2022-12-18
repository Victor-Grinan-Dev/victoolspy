import time
import threading
import multiprocessing


class Accelerate(object):
    timer_on = True
    loops: int = 1
    threads = []
    mode = "thread"  # todo: create mode multiprocessing

    def __init__(self, original_function):

        self.original_function = original_function
        self.define_loops()

    def __call__(self, *args, **kwargs):

        t1 = time.time()
        self.define_loops()

        # TODO: resolve if there is a list as an argument to be accelerated the precessing of each file

        for _ in range(self.loops - 1):
            t = threading.Thread(target=self.original_function, args=(*args,))
            t.start()

        for t in self.threads:
            t.join()

        result = self.original_function(*args, **kwargs)

        t2 = time.time() - t1
        if self.timer_on:
            print(f"executed in {t2:.2f} second(s)")

        return result

    def define_loops(self):
        """
        to make sure that loops is always correct?
        :return: nada
        """

        if self.loops == 0 or not self.loops:
            self.loops = 1

    def threader(self, data):

        for _ in range(self.loops - 1):
            t = threading.Thread(target=self.original_function, args=(*data,))
            t.start()
            return t


if __name__ == '__main__':
    family_members = ["alma", "javy", "annu", "victor", "mamma", "pappa", "mummo"]


    @Accelerate
    def display_info(*args, **kwargs):
        time.sleep(1)
        print(*args, **kwargs)


    Accelerate.loops = 100
    display_info("annu")
