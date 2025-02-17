import math
import numpy as np
from tkinter import *


# функция движения планет
def motion():
    global velocities, positions

    for planet in positions:
        if planet == "moon":
            continue  # Луна обрабатывается отдельно
        x, y = positions[planet]
        r = math.sqrt(x ** 2 + y ** 2)
        ax = -GRAVITATIONAL_CONSTANT * x / r ** 3
        ay = -GRAVITATIONAL_CONSTANT * y / r ** 3
        velocities[planet][0] += ax * TIME_STEP
        velocities[planet][1] += ay * TIME_STEP
        positions[planet][0] += velocities[planet][0] * TIME_STEP
        positions[planet][1] += velocities[planet][1] * TIME_STEP
        position_differential[planet][0] = velocities[planet][0] * TIME_STEP
        position_differential[planet][1] = velocities[planet][1] * TIME_STEP

    # Обработка движения Луны
    x_moon, y_moon = positions["moon"]
    r_moon = math.sqrt(x_moon ** 2 + y_moon ** 2)
    ax_moon = -GRAVITATIONAL_CONSTANT / 15 * x_moon / r_moon ** 3
    ay_moon = -GRAVITATIONAL_CONSTANT / 15 * y_moon / r_moon ** 3
    velocities["moon"][0] += ax_moon * TIME_STEP
    velocities["moon"][1] += ay_moon * TIME_STEP
    positions["moon"][0] += velocities["moon"][0] * TIME_STEP
    positions["moon"][1] += velocities["moon"][1] * TIME_STEP
    position_differential["moon"][0] = velocities["moon"][0] * TIME_STEP
    position_differential["moon"][1] = velocities["moon"][1] * TIME_STEP

    # двигаем планеты
    for planet in positions:
        if planet == "moon":
            continue  # Луна обрабатывается отдельно
        c.move(planets_image[planet], position_differential[planet][0] * SCALE_COEF,
               position_differential[planet][1] * SCALE_COEF)

    c.move(planets_image["moon"], (position_differential["earth"][0] + position_differential["moon"][0]) * SCALE_COEF,
                                  (position_differential["earth"][1] + position_differential["moon"][1]) * SCALE_COEF)
    c.move(planets_image["jupiter_spot"], position_differential["jupiter"][0] * SCALE_COEF,
           position_differential["jupiter"][1] * SCALE_COEF)
    c.move(planets_image["saturn_circles"], position_differential["saturn"][0] * SCALE_COEF,
           position_differential["saturn"][1] * SCALE_COEF)
    c.move(planets_image["uranus_circles"], position_differential["uranus"][0] * SCALE_COEF,
           position_differential["uranus"][1] * SCALE_COEF)
    for star in stars:
        c.move(star, position_differential["mercury"][0]*0.5, position_differential["mercury"][1]*0.5)

    root.after(15, motion)


# окно отрисовки
root = Tk()
c = Canvas(root, width=1920, height=1080, bg='#0A0A0A')
c.pack()

# константы
SCALE_COEF = 70                     # масштаб солнечной системы
TIME_STEP = 0.003
GRAVITATIONAL_CONSTANT = 4.4 * math.pi * math.pi

# константы для звезд
stars = []
stars_count = 130                   # количество звезд
stars_radius = 1.2                  # радиус звезд в пикселях

# радиусы планет (в мнимых единицах)
planet_radius = {
    "solar": 0.7 * SCALE_COEF,
    "mercury":  0.04 * SCALE_COEF,
    "venus":    0.06 * SCALE_COEF,
    "earth":   0.063 * SCALE_COEF,
    "mars":    0.055 * SCALE_COEF,
    "jupiter": 0.1 * SCALE_COEF,
    "saturn":  0.07 * SCALE_COEF,
    "uranus":   0.05 * SCALE_COEF,
    "neptune": 0.05 * SCALE_COEF,
    "moon":   0.025 * SCALE_COEF
}

# координаты солнечной системы в окне отрисовки
solar_x = 960
solar_y = 450

# начальные координаты планет и звезд относительно солнца (в мнимых единицах)
stars_position = []
initial_positions = {
    "mercury": [0, -1],
    "venus": [0, -1.5],
    "earth": [0, -2],
    "mars": [0, -2.5],
    "jupiter": [0, -3],
    "saturn": [0, -3.5],
    "uranus": [0, -4],
    "neptune": [0, -4.5],
    "moon": [0, -0.25]              # для луны относительно Земли
}

# приращение координат планет
position_differential = {
    "mercury": [0, 0],
    "venus": [0, 0],
    "earth": [0, 0],
    "mars": [0, -0],
    "jupiter": [0, 0],
    "saturn": [0, 0],
    "uranus": [0, 0],
    "neptune": [0, 0],
    "moon": [0, 0]
}

# начальные скорости планет
initial_velocities = {
    "mercury": (2 * math.pi, 0),
    "venus": (1.6 * math.pi, 0),
    "earth": (1.5 * math.pi, 0),
    "moon": (math.pi, 0),
    "mars": (1.4 * math.pi, 0),
    "jupiter": (1.3 * math.pi, 0),
    "saturn": (1.2 * math.pi, 0),
    "uranus": (1.1 * math.pi, 0),
    "neptune": (1.05 * math.pi, 0)
}

# глобальные переменные для хранения текущих позиций и скоростей
positions = {key: list(pos) for key, pos in initial_positions.items()}
velocities = {key: list(vel) for key, vel in initial_velocities.items()}

# отрисовка звезд
for i in range(stars_count):
    stars_position += [[1920*np.random.random(), 1080*np.random.random()]]
    stars.append(c.create_oval(stars_position[i][0]-stars_radius, stars_position[i][1]-stars_radius,
                               stars_position[i][0]+stars_radius, stars_position[i][1]+stars_radius,
                               fill="white"))

# отрисовка орбит
# c.create_oval(solar_x - 0.93*SCALE_COEF, solar_y - 1*SCALE_COEF, solar_x + 0.9*SCALE_COEF, solar_y + 0.84*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 1.33*SCALE_COEF, solar_y - 1.5*SCALE_COEF, solar_x + 1.3*SCALE_COEF, solar_y + 1.15*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 2.06*SCALE_COEF, solar_y - 2*SCALE_COEF, solar_x + 2.04*SCALE_COEF, solar_y + 2.1*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 2.82*SCALE_COEF, solar_y - 2.505*SCALE_COEF, solar_x + 2.78*SCALE_COEF, solar_y + 3.14*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 3.53*SCALE_COEF, solar_y - 3*SCALE_COEF, solar_x + 3.48*SCALE_COEF, solar_y + 4.07*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 4.08*SCALE_COEF, solar_y - 3.5*SCALE_COEF, solar_x + 4.03*SCALE_COEF, solar_y + 4.69*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 4.44*SCALE_COEF, solar_y - 4*SCALE_COEF, solar_x + 4.41*SCALE_COEF, solar_y + 4.89*SCALE_COEF, outline='#3D3D3D')
# c.create_oval(solar_x - 5.134*SCALE_COEF, solar_y - 4.5*SCALE_COEF, solar_x + 5.1*SCALE_COEF, solar_y + 5.82*SCALE_COEF, outline='#3D3D3D')

# отрисовка солнца и планет
planets_image = {
    "solar": c.create_oval(solar_x - planet_radius["solar"], solar_y - planet_radius["solar"],
                           solar_x + planet_radius["solar"], solar_y + planet_radius["solar"],
                           fill='#FBC413', outline='#FB7813', width=3),
    "mercury": c.create_oval(solar_x + positions["mercury"][0] * SCALE_COEF - planet_radius["mercury"],
                             solar_y + positions["mercury"][1] * SCALE_COEF - planet_radius["mercury"],
                             solar_x + positions["mercury"][0] * SCALE_COEF + planet_radius["mercury"],
                             solar_y + positions["mercury"][1] * SCALE_COEF + planet_radius["mercury"],
                             fill='#731B07', outline="#FF6A00"),
    "venus": c.create_oval(solar_x + positions["venus"][0] * SCALE_COEF - planet_radius["venus"],
                           solar_y + positions["venus"][1] * SCALE_COEF - planet_radius["venus"],
                           solar_x + positions["venus"][0] * SCALE_COEF + planet_radius["venus"],
                           solar_y + positions["venus"][1] * SCALE_COEF + planet_radius["venus"],
                           fill='#DEC478', outline="white"),
    "earth": c.create_oval(solar_x + positions["earth"][0] * SCALE_COEF - planet_radius["earth"],
                           solar_y + positions["earth"][1] * SCALE_COEF - planet_radius["earth"],
                           solar_x + positions["earth"][0] * SCALE_COEF + planet_radius["earth"],
                           solar_y + positions["earth"][1] * SCALE_COEF + planet_radius["earth"],
                           fill='#0F97FF', outline="dark blue"),
    "moon": c.create_oval(solar_x + (positions["earth"][0] + positions["moon"][0]) * SCALE_COEF - planet_radius["moon"],
                          solar_y + (positions["earth"][1] + positions["moon"][1]) * SCALE_COEF - planet_radius["moon"],
                          solar_x + (positions["earth"][0] + positions["moon"][0]) * SCALE_COEF + planet_radius["moon"],
                          solar_y + (positions["earth"][1] + positions["moon"][1]) * SCALE_COEF + planet_radius["moon"],
                          fill='#BDBDBD', outline="gray"),
    "mars": c.create_oval(solar_x + positions["mars"][0] * SCALE_COEF - planet_radius["mars"],
                          solar_y + positions["mars"][1] * SCALE_COEF - planet_radius["mars"],
                          solar_x + positions["mars"][0] * SCALE_COEF + planet_radius["mars"],
                          solar_y + positions["mars"][1] * SCALE_COEF + planet_radius["mars"],
                          fill='#C2000D', outline="#FF4D00"),
    "jupiter": c.create_oval(solar_x + positions["jupiter"][0] * SCALE_COEF - planet_radius["jupiter"],
                             solar_y + positions["jupiter"][1] * SCALE_COEF - planet_radius["jupiter"],
                             solar_x + positions["jupiter"][0] * SCALE_COEF + planet_radius["jupiter"],
                             solar_y + positions["jupiter"][1] * SCALE_COEF + planet_radius["jupiter"],
                             fill='#C1884D', outline="#CD5700"),
    "jupiter_spot": c.create_oval(solar_x + (positions["jupiter"][0]-0.02) * SCALE_COEF - planet_radius["jupiter"]*0.4,
                                  solar_y + (positions["jupiter"][1]+0.04) * SCALE_COEF - planet_radius["jupiter"]*0.3,
                                  solar_x + (positions["jupiter"][0]-0.02) * SCALE_COEF + planet_radius["jupiter"]*0.4,
                                  solar_y + (positions["jupiter"][1]+0.04) * SCALE_COEF + planet_radius["jupiter"]*0.3,
                                  fill='#CD5700', outline="gray"),
    "saturn_circles": c.create_oval(solar_x + positions["saturn"][0] * SCALE_COEF - planet_radius["saturn"]*2,
                                    solar_y + positions["saturn"][1] * SCALE_COEF - planet_radius["saturn"]*0.6,
                                    solar_x + positions["saturn"][0] * SCALE_COEF + planet_radius["saturn"]*2,
                                    solar_y + positions["saturn"][1] * SCALE_COEF + planet_radius["saturn"]*1.2,
                                    outline="#F0BD60", width=2.5),
    "saturn": c.create_oval(solar_x + positions["saturn"][0] * SCALE_COEF - planet_radius["saturn"],
                            solar_y + positions["saturn"][1] * SCALE_COEF - planet_radius["saturn"],
                            solar_x + positions["saturn"][0] * SCALE_COEF + planet_radius["saturn"],
                            solar_y + positions["saturn"][1] * SCALE_COEF + planet_radius["saturn"],
                            fill='#FAE5BF', outline="gray"),
    "uranus_circles": c.create_oval(solar_x + positions["uranus"][0] * SCALE_COEF - planet_radius["uranus"]*2.7,
                                    solar_y + positions["uranus"][1] * SCALE_COEF - planet_radius["uranus"]*0.6,
                                    solar_x + positions["uranus"][0] * SCALE_COEF + planet_radius["uranus"]*2.7,
                                    solar_y + positions["uranus"][1] * SCALE_COEF + planet_radius["uranus"]*1.5,
                                    outline="white", width=1),
    "uranus": c.create_oval(solar_x + positions["uranus"][0] * SCALE_COEF - planet_radius["uranus"],
                            solar_y + positions["uranus"][1] * SCALE_COEF - planet_radius["uranus"],
                            solar_x + positions["uranus"][0] * SCALE_COEF + planet_radius["uranus"],
                            solar_y + positions["uranus"][1] * SCALE_COEF + planet_radius["uranus"],
                            fill='#48D1CC', outline="light blue"),
    "neptune": c.create_oval(solar_x + positions["neptune"][0] * SCALE_COEF - planet_radius["neptune"],
                             solar_y + positions["neptune"][1] * SCALE_COEF - planet_radius["neptune"],
                             solar_x + positions["neptune"][0] * SCALE_COEF + planet_radius["neptune"],
                             solar_y + positions["neptune"][1] * SCALE_COEF + planet_radius["neptune"],
                             fill='#2B6CC4', outline="dark blue")
}
# запуск функции движения
motion()
root.mainloop()
