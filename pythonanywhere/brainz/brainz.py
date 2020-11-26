# -*- coding: utf-8 -*-
import random

def op_sum(a, b):
    print '%d + %d' % (a, b)
    return a + b

def op_sub(a, b):
    print '%d - %d' % (a, b)
    return a - b

def op_mult(a, b):
    print '%d * %d' % (a, b)
    return a * b

def op_div(a, b):
    print '%d * %d' % (a, b)
    return a * b


if __name__ == '__main__':
    lo = 0
    hi = 100
    ok = 0
    wrong = 0
    ops = [op_sum, op_sub, op_mult, op_div]
    top_index = len(ops) - 1
    try:
        while True:
            a = random.randint(lo, hi)
            b = random.randint(lo, hi)
            index = random.randint(0, top_index)
            op = ops[index]
            c = op(a, b)
            text = raw_input()
            try:
                answer = int(text)
            except ValueError:
                print 'Wrong. The expected answer is a number.'
                print '    You write %s. Rigth answer is %d' % (text, c)
                wrong += 1
            else:
                if answer == c:
                    print('Ok)'
                    ok += 1
                else:
                    print('Wrong.')
                    print('    You write {0:d}. Rigth answer is {1:d}'.format(answer, c))
                    wrong += 1
        print('ok {0:d} - wrong {1:d}'.format(ok, wrong))
    except KeyboardInterrupt:
        pass

print('ok {0:d} - wrong {1:d}'.format(ok, wrong))    

