#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

fig, ax = plt.subplots()

bar_width = 0.5
x = np.arange(3)

apples = ax.bar(x, fruit[0], bar_width, color='r', label='Apples')
bananas = ax.bar(x, fruit[1], bar_width, bottom=fruit[0], color='y', label='Bananas')
oranges = ax.bar(x, fruit[2], bar_width, bottom=fruit[0] + fruit[1], color='#ff8000', label='Oranges')
peaches = ax.bar(x, fruit[3], bar_width, bottom=fruit[0] + fruit[1] + fruit[2], color='#ffe5b4', label='Peaches')

ax.set_xlabel('Person')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_xticks(x)
ax.set_xticklabels(['Farrah', 'Fred', 'Felicia'])
ax.set_yticks(np.arange(0, 81, 10))
ax.legend()

plt.show()