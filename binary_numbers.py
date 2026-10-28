import tkinter as tk

# Количество двоичных регистров (разрядов)
N = 8
# Радиус кружка и расстояние между кружками
RADIUS = 30
GAP = 10

# Значения регистров: 0 или 1 (в начале все нули)
bits = [0] * N

# Размеры холста
width = N * (2 * RADIUS + GAP) + GAP
height = 2 * RADIUS + 2 * GAP

# Окно, холст для кружков и надпись для числа
root = tk.Tk()
root.title("Двоичные числа")

canvas = tk.Canvas(root, width=width, height=height, bg="lightgray")
canvas.pack()

label = tk.Label(root, text="0", font=("Times New Roman", 60))
label.pack()


def center_x(i):
    # x-координата центра i-го кружка
    return GAP + RADIUS + i * (2 * RADIUS + GAP)


def get_value():
    # переводим список из нулей и единиц в десятичное число
    value = 0
    for b in bits:
        value = value * 2 + b
    return value


def draw():
    # стираем всё и рисуем заново
    canvas.delete("all")
    y = height // 2
    for i in range(N):
        x = center_x(i)
        if bits[i] == 1:
            fill = "black"
            text_color = "white"
        else:
            fill = "white"
            text_color = "black"
        canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
                           fill=fill, outline="black")
        # цифра внутри регистра
        canvas.create_text(x, y, text=str(bits[i]), fill=text_color,
                           font=("Arial", 24))
    # обновляем число под кружками
    label.config(text=str(get_value()))


def on_click(event):
    y = height // 2
    for i in range(N):
        # проверяем, попал ли клик внутрь i-го кружка
        dx = event.x - center_x(i)
        dy = event.y - y
        if dx * dx + dy * dy <= RADIUS * RADIUS:
            bits[i] = 1 - bits[i]  # 0 становится 1, а 1 становится 0
    draw()


canvas.bind("<Button-1>", on_click)

draw()
root.mainloop()
