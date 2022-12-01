import random
from time import perf_counter


def day_1(calories_str: str):
    return max([sum([int(i) for i in c.split("\n") if i != ""]) for c in calories_str.split("\n\n")])


def day_1_2(calories_str: str):
    calories = [sum([int(i) for i in c.split("\n") if i != ""]) for c in calories_str.split("\n\n")]
    return sum(sorted(calories, reverse=True)[:3])


def random_str(n):
    elfs = {i: [random.randint(1, 1000) for _ in range(random.randint(1, 1000))] for i in range(n)}
    ret_str = ""
    maximum = 0
    for elf in elfs.values():
        for calorie in elf:
            ret_str += str(calorie) + "\n"
        if sum(elf) > maximum:
            maximum = sum(elf)
        ret_str += "\n"
    return ret_str, maximum


if __name__ == "__main__":
    # calories_str, maximum = random_str(10)
    # start = perf_counter()
    # h1 = day_1(calories_str)
    # end = perf_counter()
    # print(end - start)
    # print(h1)
    # assert h1 == maximum

    with open("Day 1/input.txt", "r") as f:
        calories_str = f.read()
    start = perf_counter()
    h1 = day_1(calories_str)
    end = perf_counter()
    print(end - start)
    print(h1)

    start = perf_counter()
    h2 = day_1_2(calories_str)
    end = perf_counter()
    print(end - start)
    print(h2)
