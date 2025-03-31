import tkinter as tk
from math import pow

# Функция для вычисления y
def f(x):
    return (pow(x, 2)) / 2 - 2
def draw_graf(width, canvas, height):
    canvas.delete("all")
    x_min, x_max = -20, 20
    y_min, y_max = -20, 20

    x_scale = width (x_max - x_min)
    y_scale = height (y_max - y_min)

    # Оси
    canvas.create_line(0, height / 2, width, height / 2, fill="black", arrow=tk.LAST)  # Ось x
    canvas.create_line(width / 2, height, width / 2, 0, fill="black", arrow=tk.LAST)  # Ось y

