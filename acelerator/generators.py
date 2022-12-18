import time
import random
import memory_profiler

# generators
# def square_nums(nums: list):
#     for i in nums:
#         yield i * i
#
#
# my_nums = square_nums([1, 2, 3, 4, 5])
# for num in my_nums:
#     print(num)

# generator comprehension
my_nums = (i * i for i in [1, 2, 3, 4, 5])
print(my_nums)  # generator object
print(list(my_nums))  # generate as a list
for num in my_nums:  # notice that this code doesnt execute, cause this was exausted
    print(num)

names = ['john', 'corey', 'adam', 'steve', 'rick', 'thomas']
majors = ['math', 'engineering', 'compsci', 'arts', 'business']


# performance comparison
def my_timer(original_function):
    from functools import wraps
    import time

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} executed execute in {t2:.2f} sec(s)")
        return original_function(*args, **kwargs)

    return wrapper_function


def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        results.append(person)
    return results


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


print(f"memory (after): {mem_profile.memory_usage_resorce()}")
