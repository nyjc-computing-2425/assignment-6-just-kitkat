from datetime import datetime
import time


# Part 1
def clock(n):
    """
    Output the time and update it once every second, for n number of seconds.

    Arguements:
    n: int - number of times to update the time

    Return:
    None
    """
    for i in range(n):
        time_data = datetime.now()
        cur_time = time_data.strftime("%H:%M:%S")
        print(cur_time, end="\r")
        time.sleep(1)

# Part 2
def lcm(a, b):
    """
    Calculates the lowest common multiple of a and b

    Arguments:
    a: int
    b: int

    Return:
    int -- the LCM of a and b
    """
    original_a, original_b = a, b
    while True:
        if a == b:
            return a
        if a < b:
            a += original_a
        else:
            b += original_b

# Part 3
def gcf(a, b):
    """
    Calculates the greatest common factor of a and b

    Arguments:
    a: int
    b: int

    Return:
    int - GCF of a and b
    """
    while True:
        if b == 0:
            return a
        r = a % b
        a, b = b, r
