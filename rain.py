import tkinter as tk
import random

# Размеры окна
WIDTH = 800
HEIGHT = 500

# Плотность дождя: сколько капель одновременно на экране
# (можно поэкспериментировать: 100 - редкий дождь, 600 - ливень)
DROPS_COUNT = 300

# Пауза между кадрами в миллисекундах
DELAY = 20

# Окно и холст со светлым фоном
root = tk.Tk()
root.title("Дождь")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="lavender")
canvas.pack()


def new_drop(y):
    # Создаём одну каплю. depth - "глубина": 0.3 - далеко, 1 - близко
    depth = random.uniform(0.3, 1.0)

    # Чем дальше капля, тем она короче, тоньше и медленнее
    drop = {
        "x": random.randint(0, WIDTH),
        "y": y,
        "length": 30 * depth,
        "speed": 12 * depth,
        "width": 1 if depth < 0.6 else 2,
    }

    # Цвет тоже зависит от глубины: дальние капли светлее
    if depth < 0.5:
        drop["color"] = "#c3a6e8"
    elif depth < 0.8:
        drop["color"] = "#9b59d0"
    else:
        drop["color"] = "#6a0dad"

    return drop


# В начале раскидываем капли по всему экрану
drops = []
for i in range(DROPS_COUNT):
    drops.append(new_drop(random.randint(0, HEIGHT)))


def animate():
    # Стираем предыдущий кадр
    canvas.delete("all")

    for i in range(len(drops)):
        d = drops[i]

        # Двигаем каплю вниз
        d["y"] += d["speed"]

        # Если капля упала за нижний край, делаем новую над экраном
        if d["y"] > HEIGHT:
            drops[i] = new_drop(random.randint(-100, 0))
            d = drops[i]

        # Рисуем каплю как вертикальную линию
        canvas.create_line(d["x"], d["y"], d["x"], d["y"] + d["length"],
                           width=d["width"], fill=d["color"])

    # Через DELAY миллисекунд вызываем эту же функцию снова
    root.after(DELAY, animate)


animate()
root.mainloop()
