import math
import random
import pygame
import pygame.gfxdraw
from pygame.locals import *

# Инициализация pygame
pygame.init()

# Константы
SCREEN_WIDTH = pygame.display.get_desktop_sizes()[0][0]
SCREEN_HEIGHT = pygame.display.get_desktop_sizes()[0][1]
SCALE_COEF = SCREEN_HEIGHT // 14  # Масштаб солнечной системы
TIME_STEP = 1
FPS = 240

# Цвета
planet_color = {
    "solar": {
        "fill": (251, 196, 19),  # Желтый цвет заливки
        "outline": (251, 120, 19),  # Оранжевая граница
    },
    "mercury": (115, 27, 7),  # Темно-красный цвет заливки
    "venus": (222, 196, 120),  # Светло-коричневый цвет заливки
    "earth": (15, 151, 255),  # Голубой цвет заливки
    "moon": (189, 189, 189),  # Серый цвет заливки
    "mars": (194, 0, 13),  # Красный цвет заливки
    "jupiter": (193, 136, 77),  # Коричневый цвет заливки
    "jupiter_spot": (205, 87, 0),  # Оранжевый цвет заливки
    "saturn": (250, 229, 191),  # Светло-коричневый цвет заливки
    "saturn_circles": (240, 189, 96),  # Оранжевая граница (кольца Сатурна)
    "uranus": (72, 209, 204),  # Бирюзовый цвет заливки
    "uranus_circles": (255, 255, 255),  # Белая граница (кольца Урана)
    "neptune": (43, 108, 196),  # Синий цвет заливки
}

BLACK = (10, 10, 10)
DARK_GRAY = (61, 61, 61)
WHITE = (255, 255, 255)

# Координаты солнечной системы в окне отрисовки
solar_x = SCREEN_WIDTH / 2
solar_y = SCREEN_HEIGHT / 2

# Начальные углы положения планет
planet_angle = {
    "mercury": math.pi / 2,
    "venus": math.pi / 2,
    "earth": math.pi / 2,
    "mars": math.pi / 2,
    "jupiter": math.pi / 2,
    "saturn": math.pi / 2,
    "uranus": math.pi / 2,
    "neptune": math.pi / 2,
    "moon": math.pi / 2
}
planets = list(planet_angle.keys())

# Угловая скорость планет
planet_angle_velocity = {
    "mercury": math.pi / 180 * 1.33 / 2,
    "venus": math.pi / 180 * 1.21 / 2,
    "earth": math.pi / 180 * 1 / 2,
    "mars": math.pi / 180 * 0.63 / 2,
    "jupiter": math.pi / 180 * 0.083 / 2,
    "saturn": math.pi / 180 * 0.06 / 2,
    "uranus": math.pi / 180 * 0.03 / 2,
    "neptune": math.pi / 180 * 0.02 / 2,
    "moon": math.pi / 180 * 4 / 2
}

# Радиусы планет
planet_radius = {
    "solar": 0.6 * SCALE_COEF,
    "mercury": 0.04 * SCALE_COEF,
    "venus": 0.06 * SCALE_COEF,
    "earth": 0.063 * SCALE_COEF,
    "mars": 0.055 * SCALE_COEF,
    "jupiter": 0.1 * SCALE_COEF,
    "saturn": 0.07 * SCALE_COEF,
    "uranus": 0.05 * SCALE_COEF,
    "neptune": 0.05 * SCALE_COEF,
    "moon": 0.025 * SCALE_COEF
}

# Орбиты планет
planet_orbit = {
    "mercury": 1,
    "venus": 1.44,
    "earth": 2,
    "mars": 2.5,
    "jupiter": 3.5,
    "saturn": 4.4,
    "uranus": 5.0,
    "neptune": 5.8,
    "moon": 0.25  # Для луны относительно Земли
}

# Словарь для хранения позиций планет на экране
positions = {planet: [0, 0] for planet in planets}

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Solar System Simulation")
clock = pygame.time.Clock()


# Функция для рисования границы круга разной толщины
def draw_outline(surface, color, center, radius, thickness):
    for i in range(0, thickness):
        pygame.gfxdraw.aacircle(surface, int(center[0]), int(center[1]), int(radius-i), color)


# Функция для рисования сглаженного круга
def draw_aa_circle(surface, color, center, radius):
    pygame.gfxdraw.aacircle(surface, int(center[0]), int(center[1]), int(radius), color)
    pygame.gfxdraw.filled_circle(surface, int(center[0]), int(center[1]), int(radius), color)


# Функция для рисования сглаженного эллипса
def draw_aa_ellipse(surface, color, center, width, height, thickness):
    pygame.gfxdraw.aaellipse(surface, int(center[0]), int(center[1]), int(width), int(height), color)
    for i in range(0, thickness):
        pygame.gfxdraw.aaellipse(surface, int(center[0]), int(center[1]), int(width) - i, int(height) - i, color)


# Функция движения планет
def planets_motion():
    global positions

    for planet in planets:
        positions[planet][0] = planet_orbit[planet] * SCALE_COEF * math.cos(planet_angle[planet])
        positions[planet][1] = -planet_orbit[planet] * SCALE_COEF * math.sin(planet_angle[planet])
        planet_angle[planet] += planet_angle_velocity[planet]/4
        if planet_angle[planet] >= 2 * math.pi:
            planet_angle[planet] -= 2 * math.pi

# Функция движения звезд
def stars_motion(stars):
    for star in stars:
        star[1] -= star[2]  # Обновление позиции звезды по Y
        if star[1] < 0:
            star[1] = SCREEN_HEIGHT
            star[0] = random.randint(0, SCREEN_WIDTH)

# Создание звезд
stars = []
for _ in range(50):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    speed, size = random.choice([[0.3, 3], [0.5, 2], [0.7, 1]])
    stars.append([x, y, speed/4, size])

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Движение планет
    planets_motion()

    # Движение звезд
    stars_motion(stars)

    # Отрисовка звезд
    for star in stars:
        pygame.draw.rect(screen, WHITE, (int(star[0]), int(star[1]), star[3], star[3]), 0)

    # Отрисовка орбит
    for planet in planets:
        pygame.gfxdraw.aacircle(screen, int(solar_x), int(solar_y), int(planet_orbit[planet] * SCALE_COEF), DARK_GRAY)

    # Отрисовка Солнца
    draw_aa_circle(screen, planet_color["solar"]["fill"], (int(solar_x), int(solar_y)), int(planet_radius["solar"]))
    draw_outline(screen, planet_color["solar"]["outline"], (int(solar_x), int(solar_y)), int(planet_radius["solar"]), 5)

    # Отрисовка планет
    for planet in planets:
        if planet == "moon":
            # Луна вращается вокруг Земли
            moon_x = solar_x + positions["earth"][0] + positions["moon"][0]
            moon_y = solar_y + positions["earth"][1] + positions["moon"][1]
            pygame.draw.circle(screen, planet_color["moon"], (int(moon_x), int(moon_y)),
                               int(planet_radius["moon"]))
        else:
            planet_x = solar_x + positions[planet][0]
            planet_y = solar_y + positions[planet][1]
            if planet == "mercury":
                draw_aa_circle(screen, planet_color["mercury"], (int(planet_x), int(planet_y)),
                               int(planet_radius["mercury"]))
            elif planet == "venus":
                draw_aa_circle(screen, planet_color["venus"], (int(planet_x), int(planet_y)),
                               int(planet_radius["venus"]))
            elif planet == "earth":
                draw_aa_circle(screen, planet_color["earth"], (int(planet_x), int(planet_y)),
                               int(planet_radius["earth"]))
            elif planet == "mars":
                draw_aa_circle(screen, planet_color["mars"], (int(planet_x), int(planet_y)),
                               int(planet_radius["mars"]))
            elif planet == "jupiter":
                draw_aa_circle(screen, planet_color["jupiter"], (int(planet_x), int(planet_y)),
                               int(planet_radius["jupiter"]))
                # Пятно на Юпитере
                pygame.draw.ellipse(screen, planet_color["jupiter_spot"],
                                    (int(planet_x - planet_radius["jupiter"] * 0.5),
                                     int(planet_y + planet_radius["jupiter"] * 0.2),
                                     int(planet_radius["jupiter"] * 0.8),
                                     int(planet_radius["jupiter"] * 0.6)))
            elif planet == "saturn":
                # Кольца Сатурна
                draw_aa_ellipse(screen, planet_color["saturn_circles"], (int(planet_x),
                                int(planet_y + planet_radius["saturn"] * 0.4)),
                                int(planet_radius["saturn"] * 3),
                                int(planet_radius["saturn"] * 1.2), 4)

                draw_aa_circle(screen, planet_color["saturn"], (int(planet_x), int(planet_y)),
                               int(planet_radius["saturn"]))
            elif planet == "uranus":
                # Кольца Урана
                draw_aa_ellipse(screen, planet_color["uranus_circles"], (int(planet_x),
                                int(planet_y + planet_radius["uranus"] * 0.5)),
                                int(planet_radius["uranus"] * 3),
                                int(planet_radius["uranus"] * 1.2), 1)

                draw_aa_circle(screen, planet_color["uranus"], (int(planet_x), int(planet_y)),
                               int(planet_radius["uranus"]))
            elif planet == "neptune":
                draw_aa_circle(screen, planet_color["neptune"], (int(planet_x), int(planet_y)),
                               int(planet_radius["neptune"]))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
