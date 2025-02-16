import math
import numpy as np
from tkinter import *


# функция движения планет
def motion():
    global vx_merkury, vy_merkury, x_merkury, y_merkury, vx_venera, vy_venera, x_venera, y_venera, vx_earth, vy_earth,\
        x_earth, y_earth, vx_mars, vy_mars, x_mars, y_mars, vx_jupyter, vy_jupyter, x_jupyter, y_jupyter, vx_saturn,\
        vy_saturn, x_saturn, y_saturn, vx_uran, vy_uran, x_uran, y_uran, vx_neptune, vy_neptune, x_neptune, y_neptune,\
        vx_moon, vy_moon, x_moon, y_moon

    # ур-я движения для меркурия
    rvector_merkury = (x_merkury**2 + y_merkury**2)**0.5
    ax_merkury = -GM * x_merkury / rvector_merkury**3
    ay_merkury = -GM * y_merkury / rvector_merkury**3
    vx_merkury += ax_merkury * dt
    vy_merkury += ay_merkury * dt
    x_merkury += vx_merkury * dt
    y_merkury += vy_merkury * dt
    dx_merkury = vx_merkury * dt
    dy_merkury = vy_merkury * dt

    # ур-я движения для венеры
    rvector_venera = (x_venera**2 + y_venera**2)**0.5
    ax_venera = -GM * x_venera / rvector_venera**3
    ay_venera = -GM * y_venera / rvector_venera**3
    vx_venera += ax_venera * dt
    vy_venera += ay_venera * dt
    x_venera += vx_venera * dt
    y_venera += vy_venera * dt
    dx_venera = vx_venera * dt
    dy_venera = vy_venera * dt

    # ур-я движения для земли
    rvector_earth = (x_earth**2 + y_earth**2)**0.5
    ax_earth = -GM * x_earth / rvector_earth**3
    ay_earth = -GM * y_earth / rvector_earth**3
    vx_earth += ax_earth * dt
    vy_earth += ay_earth * dt
    x_earth += vx_earth * dt
    y_earth += vy_earth * dt
    dx_earth = vx_earth * dt
    dy_earth = vy_earth * dt

    # ур-я движения для луны
    rvector_moon = (x_moon**2 + y_moon**2)**0.5
    ax_moon = -GM / 15 * x_moon / rvector_moon**3
    ay_moon = -GM / 15 * y_moon / rvector_moon**3
    vx_moon += ax_moon * dt
    vy_moon += ay_moon * dt
    x_moon += vx_moon * dt
    y_moon += vy_moon * dt
    dx_moon = vx_moon * dt
    dy_moon = vy_moon * dt

    # ур-я движения для марса
    rvector_mars = (x_mars**2 + y_mars**2)**0.5
    ax_mars = -GM * x_mars / rvector_mars**3
    ay_mars = -GM * y_mars / rvector_mars**3
    vx_mars += ax_mars * dt
    vy_mars += ay_mars * dt
    x_mars += vx_mars * dt
    y_mars += vy_mars * dt
    dx_mars = vx_mars * dt
    dy_mars = vy_mars * dt

    # ур-я движения для юпитера
    rvector_jupyter = (x_jupyter**2 + y_jupyter**2)**0.5
    ax_jupyter = -GM * x_jupyter / rvector_jupyter**3
    ay_jupyter = -GM * y_jupyter / rvector_jupyter**3
    vx_jupyter += ax_jupyter * dt
    vy_jupyter += ay_jupyter * dt
    x_jupyter += vx_jupyter * dt
    y_jupyter += vy_jupyter * dt
    dx_jupyter = vx_jupyter * dt
    dy_jupyter = vy_jupyter * dt

    # ур-я движения для сатурна
    rvector_saturn = (x_saturn**2 + y_saturn**2)**0.5
    ax_saturn = -GM * x_saturn / rvector_saturn**3
    ay_saturn = -GM * y_saturn / rvector_saturn**3
    vx_saturn += ax_saturn * dt
    vy_saturn += ay_saturn * dt
    x_saturn += vx_saturn * dt
    y_saturn += vy_saturn * dt
    dx_saturn = vx_saturn * dt
    dy_saturn = vy_saturn * dt

    # ур-я движения для урана
    rvector_uran = (x_uran**2 + y_uran**2)**0.5
    ax_uran = -GM * x_uran / rvector_uran**3
    ay_uran = -GM * y_uran / rvector_uran**3
    vx_uran += ax_uran * dt
    vy_uran += ay_uran * dt
    x_uran += vx_uran * dt
    y_uran += vy_uran * dt
    dx_uran = vx_uran * dt
    dy_uran = vy_uran * dt

    # ур-я движения для нептуна
    rvector_neptune = (x_neptune**2 + y_neptune**2)**0.5
    ax_neptune = -GM * x_neptune / rvector_neptune**3
    ay_neptune = -GM * y_neptune / rvector_neptune**3
    vx_neptune += ax_neptune * dt
    vy_neptune += ay_neptune * dt
    x_neptune += vx_neptune * dt
    y_neptune += vy_neptune * dt
    dx_neptune = vx_neptune * dt
    dy_neptune = vy_neptune * dt

    # двигаем планеты
    c.move(merkury, dx_merkury * scale, dy_merkury * scale)
    c.move(venera, dx_venera * scale, dy_venera * scale)
    c.move(earth, dx_earth * scale, dy_earth * scale)
    c.move(moon, (dx_earth + dx_moon) * scale, (dy_earth + dy_moon) * scale)
    c.move(mars, dx_mars * scale, dy_mars * scale)
    c.move(jupiter, dx_jupyter * scale, dy_jupyter * scale)
    c.move(jupiter_spot, dx_jupyter * scale, dy_jupyter * scale)
    c.move(saturn_circles, dx_saturn * scale, dy_saturn * scale)
    c.move(saturn, dx_saturn * scale, dy_saturn * scale)
    c.move(uran_circles, dx_uran * scale, dy_uran * scale)
    c.move(uran, dx_uran * scale, dy_uran * scale)
    c.move(neptune, dx_neptune * scale, dy_neptune * scale)

    root.after(20, motion)


# окно отрисовки
root = Tk()
c = Canvas(root, width=1920, height=1080, bg='#0A0A0A')
c.pack()

# константы
scale = 93                      # коэффициент масштабирования
dt = 0.003                      # малое приращение времени
GM = 4.4 * math.pi * math.pi    # апроксимированное произведение массы солнца на гравитационную составляющую

# звезды
stars = []
N_stars = 130                   # количество звезд
r_stars = 1.2                   # радиус звезд в пикселях

# радиусы планет (в мнимых единицах)
r_solar = 0.7
r_merkury = 0.04
r_venera = 0.06
r_earth = 0.063
r_moon = 0.025
r_mars = 0.055
r_jupiter = 0.1
r_saturn = 0.07
r_uran = 0.05
r_neptune = 0.05

# радиусы планет (в пикселях)
rad_solar = r_solar * scale
rad_merkury = r_merkury * scale
rad_venera = r_venera * scale
rad_earth = r_earth * scale
rad_moon = r_moon * scale
rad_mars = r_mars * scale
rad_jupyter = r_jupiter * scale
rad_js = rad_jupyter-16         # радиус циклона на юпитере
rad_saturn = r_saturn * scale
rad_uran = r_uran * scale
rad_neptune = r_neptune * scale

# координаты солнечной системы в окне отрисовки
x_scr0 = 960
y_scr0 = 450

# начальные координаты планет и звезд относительно солнца (в мнимых единицах)
x_stars = []
x_merkury = 0
x_venera = 0
x_earth = 0
x_mars = 0
x_jupyter = 0
x_saturn = 0
x_uran = 0
x_neptune = 0

y_stars = []
y_merkury = -1
y_venera = -1.5
y_earth = -2
y_mars = -2.5
y_jupyter = -3
y_saturn = -3.5
y_uran = -4
y_neptune = -4.5

# координаты луны относительно Земли(в мнимых единицах)
x_moon = 0
y_moon = -0.25

# начальные скорости планет
vx_merkury = 2 * math.pi
vy_merkury = 0 * math.pi

vx_venera = 1.6 * math.pi
vy_venera = 0 * math.pi

vx_earth = 1.5 * math.pi
vy_earth = 0 * math.pi

vx_moon = math.pi
vy_moon = 0 * math.pi

vx_mars = 1.4 * math.pi
vy_mars = 0 * math.pi

vx_jupyter = 1.3 * math.pi
vy_jupyter = 0 * math.pi

vx_saturn = 1.2 * math.pi
vy_saturn = 0 * math.pi

vx_uran = 1.1 * math.pi
vy_uran = 0 * math.pi

vx_neptune = 1.05 * math.pi
vy_neptune = 0 * math.pi

# отрисовка звезд
for i in range(N_stars):
    x_stars += [1920/scale*np.random.random()]
    y_stars += [1080/scale*np.random.random()]
    x_scr_stars = x_stars[i] * scale
    y_scr_stars = y_stars[i] * scale
    stars.append(c.create_oval(x_scr_stars-r_stars, y_scr_stars-r_stars, x_scr_stars+r_stars, y_scr_stars+r_stars,
                               fill="white"))

# отрисовка орбит
# c.create_oval(x_scr0 - 0.93*scale, y_scr0 - 1*scale, x_scr0 + 0.9*scale, y_scr0 + 0.84*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 1.33*scale, y_scr0 - 1.5*scale, x_scr0 + 1.3*scale, y_scr0 + 1.15*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 2.06*scale, y_scr0 - 2*scale, x_scr0 + 2.04*scale, y_scr0 + 2.1*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 2.82*scale, y_scr0 - 2.505*scale, x_scr0 + 2.78*scale, y_scr0 + 3.14*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 3.53*scale, y_scr0 - 3*scale, x_scr0 + 3.48*scale, y_scr0 + 4.07*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 4.08*scale, y_scr0 - 3.5*scale, x_scr0 + 4.03*scale, y_scr0 + 4.69*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 4.44*scale, y_scr0 - 4*scale, x_scr0 + 4.41*scale, y_scr0 + 4.89*scale, outline='#3D3D3D')
# c.create_oval(x_scr0 - 5.134*scale, y_scr0 - 4.5*scale, x_scr0 + 5.1*scale, y_scr0 + 5.82*scale, outline='#3D3D3D')

# отрисовка солнца и планет
solar = c.create_oval(x_scr0 - rad_solar, y_scr0 - rad_solar,
                      x_scr0 + rad_solar, y_scr0 + rad_solar,
                      fill='#FBC413', outline='#FB7813', width=3)
merkury = c.create_oval(x_scr0 + x_merkury * scale - rad_merkury, y_scr0 + y_merkury * scale - rad_merkury,
                        x_scr0 + x_merkury * scale + rad_merkury, y_scr0 + y_merkury * scale + rad_merkury,
                        fill='#731B07', outline="#FF6A00")
venera = c.create_oval(x_scr0 + x_venera * scale - rad_venera, y_scr0 + y_venera * scale - rad_venera,
                       x_scr0 + x_venera * scale + rad_venera, y_scr0 + y_venera * scale + rad_venera,
                       fill='#DEC478', outline="white")
earth = c.create_oval(x_scr0 + x_earth * scale - rad_earth, y_scr0 + y_earth * scale - rad_earth,
                      x_scr0 + x_earth * scale + rad_earth, y_scr0 + y_earth * scale + rad_earth,
                      fill='#0F97FF', outline="dark blue")
moon = c.create_oval(x_scr0 + (x_earth + x_moon) * scale - rad_moon, y_scr0 + (y_earth + y_moon) * scale - rad_moon,
                     x_scr0 + (x_earth + x_moon) * scale + rad_moon, y_scr0 + (y_earth + y_moon) * scale + rad_moon,
                     fill='#BDBDBD', outline="gray")
mars = c.create_oval(x_scr0 + x_mars * scale - rad_mars, y_scr0 + y_mars * scale - rad_mars,
                     x_scr0 + x_mars * scale + rad_mars, y_scr0 + y_mars * scale + rad_mars,
                     fill='#C2000D', outline="#FF4D00")
jupiter = c.create_oval(x_scr0 + x_jupyter * scale - rad_jupyter, y_scr0 + y_jupyter * scale - rad_jupyter,
                        x_scr0 + x_jupyter * scale + rad_jupyter, y_scr0 + y_jupyter * scale + rad_jupyter,
                        fill='#C1884D', outline="#CD5700")
jupiter_spot = c.create_oval(x_scr0 + (x_jupyter-0.05) * scale - rad_js, y_scr0 + y_jupyter * scale - rad_js,
                             x_scr0 + x_jupyter * scale + rad_js, y_scr0 + (y_jupyter+0.09) * scale + rad_js,
                             fill='#CD5700', outline="gray")
saturn_circles = c.create_oval(x_scr0 + x_saturn * scale - rad_saturn*2, y_scr0 + y_saturn * scale - rad_saturn*0.6,
                               x_scr0 + x_saturn * scale + rad_saturn*2, y_scr0 + y_saturn * scale + rad_saturn*1.2,
                               outline="#F0BD60", width=2.5)
saturn = c.create_oval(x_scr0 + x_saturn * scale - rad_saturn, y_scr0 + y_saturn * scale - rad_saturn,
                       x_scr0 + x_saturn * scale + rad_saturn, y_scr0 + y_saturn * scale + rad_saturn,
                       fill='#FAE5BF', outline="gray")
uran_circles = c.create_oval(x_scr0 + x_uran * scale - rad_uran*2.7, y_scr0 + y_uran * scale - rad_uran*0.6,
                             x_scr0 + x_uran * scale + rad_uran*2.7, y_scr0 + y_uran * scale + rad_uran*1.5,
                             outline="white", width=1)
uran = c.create_oval(x_scr0 + x_uran * scale - rad_uran, y_scr0 + y_uran * scale - rad_uran,
                     x_scr0 + x_uran * scale + rad_uran, y_scr0 + y_uran * scale + rad_uran,
                     fill='#48D1CC', outline="light blue")
neptune = c.create_oval(x_scr0 + x_neptune * scale - rad_neptune, y_scr0 + y_neptune * scale - rad_neptune,
                        x_scr0 + x_neptune * scale + rad_neptune, y_scr0 + y_neptune * scale + rad_neptune,
                        fill='#2B6CC4', outline="dark blue")

# запуск функции движения
motion()
root.mainloop()
