import random

def op_sum(a, b):
    print(f'{a} + {b}')
    return a + b

def op_sub(a, b):
    print(f'{a} - {b}')
    return a - b

def op_mult(a, b):
    print(f'{a} * {b}')
    return a * b

def op_div(a, b):
    print(f'{a} / {b}')
    return a / b

minimum = 0
maximum = 100
ok = 0
wrong = 0
ops = [op_sum, op_sub, op_mult, op_div]
top_index = len(ops) - 1
try:
    while True:
        a = random.randint(minimum, maximum)
        b = random.randint(minimum, maximum)
        index = random.randint(0, top_index)
        op = ops[index]
        c = op(a, b)
        text = input()
        try:
            answer = int(text)
        except ValueError:
            print('Wrong. The expected answer is a number.')
            print(f'    You write {text}. Rigth answer is {c}')
            wrong += 1
        else:
            if answer == c:
                print('Ok')
                ok += 1
            else:
                print('Wrong.')
                print(f'    You write {answer:d}. Rigth answer is {c:d}')
                wrong += 1
    print('ok {ok:d} - wrong {wrong:d}')
except KeyboardInterrupt:
    pass
except EOFError:
    pass
print('ok {ok:d} - wrong {wrong:d}')

