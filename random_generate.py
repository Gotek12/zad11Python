from random import randint
from random import gauss
from math import sqrt

def generate_random_int(size, range = 1000):
    numbers = []
    for x in xrange(size):
        numbers.append(randint(0,range))
    return numbers

def generate_random_int_in_range(size, bottom = 100, top = 1000):
    numbers = []
    for x in xrange(size):
        numbers.append(randint(bottom,top))
    return numbers

def generate_almost_sorted_int(size, range = 1000, how_far = 1):
    numbers = generate_random_int(size, range)
    numbers.sort()
    for x in xrange(size-how_far):
        current = randint(0,how_far)
        if(current != 0): numbers[x], numbers[x+current] = numbers[x+current], numbers[x]
        x+= current+1
    return numbers

def generate_almost_reverse_sorted_int(size, range = 1000, how_far = 1):
    numbers = generate_almost_sorted_int(size,range,how_far)
    numbers.reverse()
    return numbers

def generate_gaussian_float(size,mu = 0, sigma = 1):
    numbers = []
    for x in xrange(size):
        numbers.append(gauss(mu,sigma))
    return numbers

def generate_recurring_int(size):
    return generate_random_int(size, sqrt(size))
