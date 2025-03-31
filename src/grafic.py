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
    canvas.create_line(width / 2, height, width / 2, 0, fill="black", arrow=tk.LAST) # Ось y

    canvas.create_text(width / 2 + 10, height / 2 - 10, text = "0", ancho=tk.W)
    canvas.create_text(width / 2 + 10, 10, text = "y", anchor=tk.W)
    canvas.create_text(width - 10, height / 2 + 10, text = "x", anchor=tk.E)

    canvas.create_oval(width / 2 - 3, height / 2 - 3, width / 2 + 3, height / 2 + 3, fill="white") # Точка О

    # Рисуем график функции
    for x in range(int(x_min * x_scale), int(x_max * x_scale)):
        x1 = x / x_scale
        y1 = f(x1)
        x2 = (x + 1) / x_scale
        y2 = f(x2)
        canvas.create_line(
            (x1 - x_min) * x_scale, height - (y1 - y_min) * y_scale,
            (x2 - x_min) * x_scale, height - (y2 - y_min) * y_scale,
            fill="blue"
        )

