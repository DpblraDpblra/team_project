import matplotlib.pyplot as plt

def plot_data(data):
    '''Функция визуализации пустые данные
    генерируют ValueError'''
    if not data:
        raise ValueError('data must not NULL')
    plt.plot(data)
    plt.show()
