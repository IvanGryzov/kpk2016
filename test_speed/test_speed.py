from random import choice, randint
import timeit

test_len = [100,1000,10000,100000,1000000]
num_of_tests = 10

def test_pop(n):
    test_list = [randint(1, 10000) for i in range(n)]
    t=test_list.pop()


for num_of_elements in test_len:
    #test_pop(num_of_elements)
    #print(timeit.Timer(setup='test_pop('+str(num_of_elements) + ")").repeat(10, num_of_tests))
    #timeit.timeit("test_pop(" + str(num_of_elements) + ")", number=num_of_tests)
    print(num_of_elements, timeit.timeit("test_pop(num_of_elements)","from __main__ import test_pop, num_of_elements", number=num_of_tests))


