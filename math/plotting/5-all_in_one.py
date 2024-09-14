#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig, axs = plt.subplots(3, 2, figsize=(12, 12))

axs[0, 0].plot(y0)
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')
axs[0, 0].set_title('Plot 1')
axs[0, 0].tick_params(axis='x', labelsize='x-small')
axs[0, 0].tick_params(axis='y', labelsize='x-small')

axs[0, 1].scatter(x1, y1)
axs[0, 1].set_xlabel('X')
axs[0, 1].set_ylabel('Y')
axs[0, 1].set_title('Plot 2')
axs[0, 1].tick_params(axis='x', labelsize='x-small')
axs[0, 1].tick_params(axis='y', labelsize='x-small')

axs[1, 0].plot(x2, y2)
axs[1, 0].set_xlabel('Time (years)')
axs[1, 0].set_ylabel('Fraction Remaining')
axs[1, 0].set_title('Plot 3')
axs[1, 0].tick_params(axis='x', labelsize='x-small')
axs[1, 0].tick_params(axis='y', labelsize='x-small')

axs[1, 1].plot(x3, y31, color='r', linestyle='--', label='C-14')
axs[1, 1].plot(x3, y32, color='g', label='Ra-226')
axs[1, 1].set_xlabel('Time (years)')
axs[1, 1].set_ylabel('Fraction Remaining')
axs[1, 1].set_title('Plot 4')
axs[1, 1].tick_params(axis='x', labelsize='x-small')
axs[1, 1].tick_params(axis='y', labelsize='x-small')
axs[1, 1].legend(loc='upper right', prop={'size': 'x-small'})

axs[2, 0].hist(student_grades, bins=np.arange(0, 110, 10), edgecolor='black')
axs[2, 0].set_xlabel('Grades')
axs[2, 0].set_ylabel('Number of Students')
axs[2, 0].set_title('Plot 5')
axs[2, 0].tick_params(axis='x', labelsize='x-small')
axs[2, 0].tick_params(axis='y', labelsize='x-small')

axs[2, 1].axis('off')

fig.suptitle('All in One', fontsize='x-small')
plt.tight_layout()
plt.show()