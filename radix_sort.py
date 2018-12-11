
from random_generate import generate_random_int_in_range as gen
from time import time

def radix_sort(numbers):
    max_value = max(numbers)
    current_pow = 0
    buckets = [[],[],[],[],[],[],[],[],[],[]]
    while 10**current_pow <= max_value:
        it = 0
        while len(numbers) != 0:
            current = numbers[-1]
            numbers.pop()
            if(current < 10**current_pow): buckets[0].append(current)
            else: buckets[(current/10**current_pow)%10].append(current)
        for x in xrange(9):
            while len(buckets[x]) != 0:
                current = buckets[x][-1]
                buckets[x].pop()
                numbers.append(current)
        current_pow+=1
    return numbers


# czesc testowa

size = 10000
bottom = 100
top = 10000000

numbers = gen(size,bottom,top)
start = time()
radix_sort(numbers)
end = time()
print numbers
print "\n\nTime for {0} elements in range ({1},{2}) : {3}\n\n".format(size,bottom,top,end-start)
