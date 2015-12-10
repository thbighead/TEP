# Encontrar a maior seuquencia de collatz gerada pelos numeros dados em
# um certo intervalo de numeros inteiros. A memoizacaum guardara g(x),
# sendo x o numero que gerarah a sequencia de collatz e o g(x) o
# tamanho dessa sequencia gerada
from time import time


memo = {}
max_memo = 1000
biggest_memo_key = 0

def collatz_sequence_printer(n):
    sequence = [n]

    if n > 1:
        sequence += collatz_sequence_printer(n/2 if n%2==0 else 3*n+1)

    return sequence


def collatz_sequence(n, my_range, greatest_range_length):
    sequence_size = 1

    # the first n which comes is the only one which can be the greatest, all other n called by the recursion can't generate greater sequences than it
    try:
        # print 'collatz_sequence: deleting ' + str(n)
        # del my_range[my_range.index(n)]  # index function may delay the application
        del my_range[greatest_range_length - n]  # better than search n index in a list to delete it
    except:
        pass
    if n > 1:
        try:
            sequence_size = memo[n]
        except:
            if binary_two_powered_test(n):
                sequence_size += calc_two_powered_collatz_len(n)
            else:
                sequence_size += collatz_sequence(n/2 if n%2==0 else 3*n+1, my_range, greatest_range_length)
                memo_add(n, sequence_size)

    return sequence_size


def collatz_greatest_sequence(a, b):
    start = time()

    greatest_sequence_length = 0  # greatest collatz sequence length
    my_range = dict(zip(xrange(b), xrange(b, a - 1, -1)))  # my_range in descending order may delete more cases
    for new_number in my_range.values():
        # print new_number
        # print my_range
        # raw_input()
        new_length = collatz_sequence(new_number, my_range, b)
        if new_length > greatest_sequence_length:
            greatest_sequence_length = new_length
            greatest_sequence_number = new_number

    elapsed_time = time() - start
    print 'With a length of ' + str(greatest_sequence_length) + ', the greatest Collatz sequence is: '
    print collatz_sequence_printer(greatest_sequence_number)
    print 'generated by the number ' + str(greatest_sequence_number)

    print ('Time: %d' % elapsed_time)


def binary_two_powered_test(x):  # tests if an integer is a two powered number
    # print x
    bin_x = bin(x)
    if bin_x.count('1') == 1:
        return True
    return False


def calc_two_powered_collatz_len(x):
    return len(bin(x)) - 3  # ignoring the first element of list and the two first characters of python's binary represatation ("0b")


def memo_add(new_number, new_sequence_size):
    global biggest_memo_key
    memo_len = len(memo)
    if memo_len >= max_memo:
        if biggest_memo_key == 0:
            biggest_memo_key = max(memo)  # max function may delay the application
        if new_number < biggest_memo_key:
            del memo[biggest_memo_key]
            biggest_memo_key = 0
            memo[new_number] = new_sequence_size
    elif memo_len < max_memo:
        memo[new_number] = new_sequence_size


# collatz_greatest_sequence(6, 8)
collatz_greatest_sequence(100000, 1000000)  # it takes about 350 secs to finish
# collatz_greatest_sequence(100, 1000)
# collatz_greatest_sequence(1000, 10000)
# print memo