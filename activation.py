import math
import numpy as np
from is_number import is_number

def calc_sig(x):
    return 1 / (1 + math.exp(-x))

def calc_elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)

def calc_activation_func(x: float, act_name: str) -> float:
    if act_name == 'sigmoid':
        return 1 / (1 + np.exp(-x))
    elif act_name == 'relu':
        return np.maximum(0, x)
    elif act_name == 'elu':
        alpha = 0.01
        return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def exercise2():
    x = input('Enter x: ')
    if not is_number(x):
        print('x must be a number')
        return 
    
    activation_func = input('Enter activation function (sigmoid/relu/elu): ')
    x = float(x)
    result = calc_activation_func(x, activation_func)
    if (result):
        print(f'{activation_func}: f({x}) = {result}')
    else:
        print(f'{activation_func} is not supported')


if __name__ == '__main__':
    exercise2()
    
    assert round(calc_sig(3), 2) == 0.95
    print(round(calc_sig(2), 2))

    assert round(calc_elu(1)) == 1
    print(round(calc_elu(-1), 2))

    assert calc_activation_func(x=1, act_name='relu') == 1
    print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))
    print(calc_activation_func(x=1, act_name='belu'))