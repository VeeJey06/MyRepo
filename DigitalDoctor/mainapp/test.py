import matplotlib.pyplot as mp
import pandas as pd
import numpy as np


class Test:
    def __init__(self):
        self.data = pd.read_csv("./Resources/Users.csv")

    def learn(self):
        t = np.arange(1, 5, 0.5)
        mp.plot(t,t, 'r--', t, t**2, 'bs', 'g^')
        mp.show()

    def plot_test(self):
        ax = mp.axes(projection='3d')
        z = np.array(self.data['risk']).reshape(1, -1)
        y = np.array(self.data['risk']).reshape(1, -1)
        x = np.array(self.data.drop("risk", axis=1)).reshape(1, -1)

        ax.scatter3D(x, y, z, c=z, cmap='Greens')


if __name__ == '__main__':
    a = Test()
    a.learn()