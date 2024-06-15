import numpy as np

def calc_ae(y, y_hat):
    if not isinstance(y, (int, float)) or not isinstance(y_hat, (int, float)):
        raise ValueError('Input must be numeric')
    return np.abs(y - y_hat)

def calc_se(y, y_hat):
    if not isinstance(y, (int, float)) or not isinstance(y_hat, (int, float)):
        raise ValueError('Input must be numeric')
    return (y - y_hat) ** 2

def md_nre_single_sample(y, y_hat, n, p):
    y_root = y ** (1/n)
    y_hat_root = y_hat ** (1/n)
    difference = y_root - y_hat_root
    loss = difference ** p
    return loss

def exercise3():
    n_samples = input('Input number of samples (int) which are generated: ')
    if not n_samples.isnumeric():
        print('Number of samples must be an integer number')
        return

    loss_name = input('Input loss name: ')

    n_samples = int(n_samples)

    loss = 0
    for i in range(n_samples):
        target = np.random.rand() * 10
        pred = np.random.rand() * 10

        if loss_name == 'MAE':
            loss += calc_ae(target, pred)
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss += calc_se(target, pred)
        
        print(f'loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}')

    loss /= n_samples
    if loss_name == 'RMSE':
        loss = np.sqrt(loss)
    print(f'final {loss_name}: {loss}')
    

if __name__ == '__main__':
    exercise3()
    
    assert calc_ae(1, 6) == 5
    print(calc_ae(2, 9))

    assert calc_se(4, 2) == 4
    print(calc_se(2, 1))

    print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))
    print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))
    print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))
    print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))