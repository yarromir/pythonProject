# Нарисовать график функций (линейный). Например график зависимости градуссов цельсия от фарингейта.
# Внести случаную ошибку в формулу. Построить новый график.
# *Попробовать решить данную задачу через LinearSVR*

import pandas as pd
import matplotlib.pyplot as plt

cel = list(range(-20, 21))
fah = list()
fah_wrong = list()

for c in cel:
    f = round((c * 1.8 + 32), 1)
    fah.append(f)

for c in cel:
    f = round((c * 1.5 + 16), 1)
    fah_wrong.append(f)

df = pd.DataFrame(zip(cel, fah, fah_wrong), columns=['C', 'F', 'Fw'])

plt.plot(df['C'], df['F'], color='r')
plt.plot(df['C'], df['Fw'], color='y')
plt.scatter(df['C'], df['F'])
plt.scatter(df['C'], df['Fw'])
plt.xlabel('Celsius')
plt.ylabel('Fahrenheit')
plt.grid()
plt.show()
