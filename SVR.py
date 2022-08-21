# Нарисовать график функций (линейный). Например график зависимости градуссов цельсия от фарингейта.
# Внести случаную ошибку в формулу. Построить новый график.
# *Попробовать решить данную задачу через LinearSVR*

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

cel = list(range(-20, 21))
fah = list()

for c in cel:
    f = round((c * 1.8 + 32), 1)
    fah.append(f)

df = pd.DataFrame(zip(cel, fah), columns=['C', 'F'])

X = df['C']
Y = df['F']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=None, train_size=0.2)

regressor = SVR(kernel='rbf')
regressor.fit(X, Y)

y_pred = regressor.predict(6.5)
y_pred = Y.inverse_transform(y_pred)

X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, Y, color='red')
plt.plot(X_grid, regressor.predict(X_grid), color='blue')
plt.xlabel('Celsius')
plt.ylabel('Fahrenheit')
plt.show()