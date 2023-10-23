import matplotlib as mpl
import matplotlib.pyplot as plt


# Graficos em Linhas

# plt.plot([1,2,3,4], [5,6,7,8])

# x = [1,2,3]
# y = [6,7,8]


# plt.plot(x,y)
# plt.xlabel('variavel 1')
# plt.ylabel('variavel 2')
# plt.title('Grafico Plot')
# plt.show()

# plt.plot([4,5], [6,7])
# plt.show()

# Graficos em Barras

# x1 = [2,4,6,8,10]
# y1 = [6,7,8,2,4]

# plt.bar(x1, y1, label = 'Barras', color='red')
# plt.legend()
# plt.show()

# # ----- #
# x2 = [1,3,5,7,8]
# y2 = [7,8,2,4,2]

# plt.bar(x1, y2, label = 'Lista1', color='blue')
# plt.bar(x2, y2, label = 'Lista2', color='gray')
# plt.legend()
# plt.show()

# # idade em barras
# idade = [22,43,56,43,6,7,34,56,44,74,23,43,76,23]

# ida = [x for x in range(len(idade))]

# plt.bar(ida, idade)
# plt.show()

# # lista de bins

# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(idade, bins, histtype= 'bar', rwidth=0.8)
# plt.show()

# plt.hist(idade, bins, histtype= 'stepfilled', rwidth= 0.8)
# plt.show()

# Grafico de Dispersão

# x = [1,2,3,4,5,6,7,8]
# y = [5,2,5,4,6,7,8,4]

# plt.scatter(x, y, label = 'Pontos', color = 'black', marker = 'o')
# plt.legend()
# plt.show()

# dias = [1,2,3,4,5]
# dormir = [7,8,6,77,7]
# comer = [2,3,4,5,3]
# trabalhar = [7,8,7,2,2]
# passear = [8,5,7,8,13]

# plt.stackplot(dias, dormir, comer, trabalhar, passear, colors=['m', 'c', 'r', 'k', 'b'])
# plt.show()

# Grafico de Pizza

# fatias = [7, 2, 2, 13]
# atividade = ['dormir', 'comer', 'passear', 'trabalhar']
# cores = ['olive', 'lime', 'violet', 'royalblue']

# plt.pie(fatias, labels= atividade, colors= cores, startangle= 90,
# shadow=True, explode=(0.1,0.2,0.1,0.1))
# plt.show()

# Graficos em Linha
from pylab import *


# x = linspace(0, 5, 10)
# y = x ** 2

# fig = plt.figure()

# axes = fig.add_axes([0, 0, 0.8, 0.8])

# axes.plot(x, y, 'r')

# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_title('Grafico de Linhas')
# plt.show()

# x = linspace(0, 5, 10)
# y = x ** 3

# fig = plt.Figure()

# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# axes1.plot(x, y, 'r')
# axes1.set_xlabel('x')
# axes1.set_ylabel('y')
# axes1.set_title('Figura Principal');



# axes2.plot(x, y, 'g')
# axes2.set_xlabel('x')
# axes2.set_ylabel('y')
# axes2.set_title('Figura Secundaria');

# Histogramas com Matplitlib em python
from mpl_toolkits.mplot3d.axes3d import Axes3D
import random
import numpy as np
import pandas as pd
import matplotlib as mat
import matplotlib.pyplot as plt
import warnings
import seaborn as sea
warnings.filterwarnings('ignore')

# n = np.ramdom.randn(10000)

# fig, axes = plt.subplts(1, 2, figsize= (12,4))

# axes[0].hist(n)
# axes[0].set_title("Histograma Padrão")
# axes[0].set_title(min(n), (max(n)))

# axes[1].hist(n, cumulative = True, bins = 50)
# axes[1].set_title("Histograma Cumulativo")
# axes[1].set_xlim((min(n), max(n)))

# ----------------#

# dados = sea.load_dataset("tips")

# dados.head()

# sea.jointplot(data = dados, x = "total_bill", y = "tip", kind= "reg")

# sea.lmplot(data = dados, x = "total_bill", y = "tip", col= "smoker")

# df = pd.DataFrame()

# df["idade"] = random.sample(range(20, 100), 30)
# df["peso"] = random.sample(range(55, 150), 30)

# df.shape

# df.head()

sea.set(style = 'ticks')

sea.lmplot(x = 'altura',
           y = 'peso',
           data = dados,
           hue = 'flag_fumante',
           palette = ['tab: blue', 'tab: orange'],
           height = 7)
plt.xlabel('altura (cm)')
plt.ylabel('peso (kg)')
plt.title("Relação entre os dois")

sea.despine()

pt.show()