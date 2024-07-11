import matplotlib.pyplot as plt # библиотека для графиков
import numpy as np # используется только для массивов
import random

# Считает значения функции для построения графика
# Принимает функцию, левую и правую границу, а также количество точек для графика
def get_x_y(func, a, b, count = 10000):
    xx = np.zeros(count)
    yy = np.zeros(count)
    for i in range(count):
        x = a + (b - a) / count * i
        xx[i] = x
        yy[i] = func(x)
    return (xx, yy)

# Строит интегральную сумму для функции
# Принимает функцию, левую и правую границы, количество отрезков разбиения, а также модификатор разбиения
def get_int_sums(func, a, b, n = 50, mode = "left"):
    sum = 0
    xx = np.zeros(n)
    yy = np.zeros(n)
    segments = np.zeros((n, 3))
    for i in range(n):
        left = a + (b - a) / n * i # левая граница текущего отрезка разбиения
        right = a + (b - a) / n * (i + 1) # правая граница текущего отрезка разбиения
        if (mode == "left"):
            x = left
        elif (mode=="right"):
            x = right
        elif (mode == "mid"):
            x = (left + right) / 2
        elif (mode == "random"):
            x = random.uniform(left, right)
        else:
            raise Exception("Invalid mode")
        y = func(x)
        xx[i] = x
        yy[i] = y
        segments[i] = (left, right, y)
        sum += y * (right - left)
    return (sum, (xx, yy), segments)

# По данной функции, левой и правой границе, а также количества отрезков разбиения и модификатору
# считает интегральную сумму, строит график и сохраняет его в file 
def plot_integral(func, a = -1, b = 2, n = 50, mode = "left", file = "graf.png"):
    fig, ax = plt.subplots()
    sum, (xx1, yy1), segments = get_int_sums(func, a, b, n = n, mode = mode)
    xx2, yy2 = get_x_y(func, a, b) 
    ax.plot(xx2, yy2, color = "red") # построение графика функции

    for i in segments: # визуализация интегральных сумм
        ax.bar((i[0] + i[1]) / 2, i[2], (i[1] - i[0]), color = "#42AAFF", alpha = 1) # средняя по x, высота, ширина

    ax.plot(xx1, yy1, '.', color = "black") # точки для интегральных сумм

    fig.savefig(file)

    return sum

# Функция в задаче
def func(x):
    return 3 * x - 2 * x * x

print("Please enter 2 numbers separated by a space - the boundaries of the segment " +
	"on which to calculate the integral sums (inclusive)")
a, b = input().split()
print("Please enter the split size")
n = int(input())
print("Please enter the equipment selection method (left / right / mid / random)")
mode = input()
print("Finally, please enter the name of the output file")
file = input()

print("Sum = " + str(plot_integral(func, a = int(a), b = int(b), n = n, mode = mode, file = file)))