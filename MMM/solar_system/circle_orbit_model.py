import math
import random
import numpy as np
import threading
from tkinter import *


# функция движения планет
def planets_motion():
    global positions

    for planet in planets:
        positions[planet][0] = -planet_orbit[planet]*SCALE_COEF * math.cos(planet_angle[planet])
        positions[planet][1] = -planet_orbit[planet]*SCALE_COEF * math.sin(planet_angle[planet])
        c.coords(planets_image[planet], solar_x + positions[planet][0] - planet_radius[planet],
                                        solar_y + positions[planet][1] - planet_radius[planet],
                                        solar_x + positions[planet][0] + planet_radius[planet],
                                        solar_y + positions[planet][1] + planet_radius[planet])
        planet_angle[planet] += planet_angle_velocity[planet]
        if planet_angle[planet] >= 2 * math.pi:
            planet_angle[planet] -= 2 * math.pi

    c.coords(planets_image["jupiter_spot"], solar_x + positions["jupiter"][0] - 2 - planet_radius["jupiter"]*0.5,
                                            solar_y + positions["jupiter"][1] + 4 - planet_radius["jupiter"]*0.3,
                                            solar_x + positions["jupiter"][0] - 2 + planet_radius["jupiter"]*0.5,
                                            solar_y + positions["jupiter"][1] + 4 + planet_radius["jupiter"]*0.3)

    c.coords(planets_image["saturn_circles"], solar_x + positions["saturn"][0] - planet_radius["saturn"] * 2,
                                              solar_y + positions["saturn"][1] - planet_radius["saturn"] * 0.6,
                                              solar_x + positions["saturn"][0] + planet_radius["saturn"] * 2,
                                              solar_y + positions["saturn"][1] + planet_radius["saturn"] * 1.2)

    c.coords(planets_image["uranus_circles"], solar_x + positions["uranus"][0] - planet_radius["uranus"]*2.7,
                                              solar_y + positions["uranus"][1] - planet_radius["uranus"]*0.6,
                                              solar_x + positions["uranus"][0] + planet_radius["uranus"]*2.7,
                                              solar_y + positions["uranus"][1] + planet_radius["uranus"]*1.5)

    c.coords(planets_image["moon"], solar_x + positions["earth"][0] + positions["moon"][0] - planet_radius["moon"],
                                    solar_y + positions["earth"][1] + positions["moon"][1] - planet_radius["moon"],
                                    solar_x + positions["earth"][0] + positions["moon"][0] + planet_radius["moon"],
                                    solar_y + positions["earth"][1] + positions["moon"][1] + planet_radius["moon"])

    root.after(10, planets_motion)

# функция движения звезд
def stars_motion():
    for star in stars_image:
        diameter = round(c.coords(star)[3] - c.coords(star)[1])
        if diameter == 4:
            if c.coords(star)[3] < 0:
                c.move(star, stars_velocity2["2px"][0] * TIME_STEP * SCALE_COEF, c.winfo_height())
            else:
                c.move(star, stars_velocity2["2px"][0] * TIME_STEP * SCALE_COEF,
                       stars_velocity2["2px"][1] * TIME_STEP * SCALE_COEF)
        elif diameter == 3:
            if c.coords(star)[3] < 0:
                c.move(star, stars_velocity2["1.5px"][0] * TIME_STEP * SCALE_COEF, c.winfo_height())
            else:
                c.move(star, stars_velocity2["1.5px"][0] * TIME_STEP * SCALE_COEF,
                       stars_velocity2["1.5px"][1] * TIME_STEP * SCALE_COEF)
        elif diameter == 2:
            if c.coords(star)[3] < 0:
                c.move(star, stars_velocity2["1px"][0] * TIME_STEP * SCALE_COEF, c.winfo_height())
            else:
                c.move(star, stars_velocity2["1px"][0] * TIME_STEP * SCALE_COEF,
                       stars_velocity2["1px"][1] * TIME_STEP * SCALE_COEF)
    root.after(15, stars_motion)


# окно отрисовки
root = Tk()
root.state('zoomed')
c = Canvas(root, width=1920, height=1080, bg='#0A0A0A')
c.pack()

# константы
SCALE_COEF = 83                    # масштаб солнечной системы
TIME_STEP = 0.003

# координаты солнечной системы в окне отрисовки
solar_x = c.winfo_screenwidth()/2
solar_y = c.winfo_screenheight() * (1/2 -1/25)

# начальные углы положения планет
planet_angle = {
    "mercury": math.pi/2,
    "venus":    math.pi/2,
    "earth":   math.pi/2,
    "mars":    math.pi/2,
    "jupiter": math.pi/2,
    "saturn":  math.pi/2,
    "uranus":   math.pi/2,
    "neptune": math.pi/2,
    "moon":   math.pi/2
}
planets = list(planet_angle.keys())

# угловая скорость планет
planet_angle_velocity = {
    "mercury":  math.pi/180*1.33/2,
    "venus":    math.pi/180*1.21/2,
    "earth":   math.pi/180*1/2,
    "mars":    math.pi/180*0.63/2,
    "jupiter": math.pi/180*0.083/2,
    "saturn":  math.pi/180*0.06/2,
    "uranus":   math.pi/180*0.03/2,
    "neptune": math.pi/180*0.02/2,
    "moon":   math.pi/180*4/2
}

# радиусы планет (в мнимых единицах)
planet_radius = {
    "solar": 0.6 * SCALE_COEF,
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

# орбиты планет
planet_orbit = {
    "mercury": 1,
    "venus": 1.44,
    "earth": 2,
    "mars": 2.5,
    "jupiter": 3.5,
    "saturn": 4.4,
    "uranus": 5.,
    "neptune": 5.8,
    "moon": 0.25              # для луны относительно Земли
}

# словарь для хранения позиций планет на экране
positions = {
    "mercury": [0, 0],
    "venus": [0, 0],
    "earth": [0, 0],
    "mars": [0, 0],
    "jupiter": [0, 0],
    "saturn": [0, 0],
    "uranus": [0, 0],
    "neptune": [0, 0],
    "moon": [0, 0]
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

# константы для звезд
stars_image = []
stars_count = 50                   # количество звезд
stars_radius = [1, 1.5, 2]         # радиус звезд в пикселях

# начальные координаты звезд
stars_position = []

# скорости звезд
stars_velocity2 = {
    "1px": [0, -2.5],
    "1.5px": [0, -1.5],
    "2px": [0, -0.75]
}

# отрисовка звезд
for i in range(stars_count):
    stars_position += [[1920*np.random.random(), 1080*np.random.random()]]
    star_radius = stars_radius[random.randint(0, 2)]
    stars_image.append(c.create_oval(stars_position[i][0]-star_radius, stars_position[i][1]-star_radius,
                                     stars_position[i][0]+star_radius, stars_position[i][1]+star_radius,
                                     fill="white"))

# отрисовка орбит
for planet in planets:
    c.create_oval(solar_x - planet_orbit[planet] * SCALE_COEF,
                  solar_y - planet_orbit[planet] * SCALE_COEF,  # орбита меркурия
                  solar_x + planet_orbit[planet] * SCALE_COEF,
                  solar_y + planet_orbit[planet] * SCALE_COEF, outline='#3D3D3D')

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

# запуск функций движения
planets_thread = threading.Thread(target=planets_motion)
stars_thread = threading.Thread(target=stars_motion)
planets_thread.start()
stars_thread.start()
root.mainloop()
