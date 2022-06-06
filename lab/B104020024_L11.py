import numpy as np # 製作資料
import matplotlib.pyplot as plt


x = np.linspace(0, np.pi*4, 51)
y = np.sin(x)
with plt.style.context('fivethirtyeight'):
    plt.plot(x, y)
    plt.plot(x, np.cos(x), c='g')
    plt.ylim(-2, 2)
    plt.ylabel("hi there")
    plt.title('sin cos Plot lab', size=30, color='r')
    plt.legend(['sin', 'cos']) # 顯示 圖例
    plt.show()

data = {'a': np.arange(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)

with plt.style.context('dark_background'):
    
    plt.hist(data['b'])
    plt.xlim(-20, 100)
    plt.ylim(0, 10)
    plt.title('hihi', size=30, color='b')
    plt.show()

