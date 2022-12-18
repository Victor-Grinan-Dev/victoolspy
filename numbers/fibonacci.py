def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


def fibonacci(x):
    return [fibonacci_of(n) for n in range(x)]


class Fibonacci:
    closers = [0, 1]

    def __init__(self, number):
        self.n = number

    def fibonacci_of(self):
        if self.n in self.closers:  # Base case
            return self.n
        return fibonacci_of(self.n - 1) + fibonacci_of(self.n - 2)  # Recursive case
