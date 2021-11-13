import pygame
from Car import Car

WIDTH = 1500
HEIGHT = 1000
FPS = 60

BACKGROUND = (0, 150, 200)

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cars")
clock = pygame.time.Clock()
draw_tool = pygame.draw


cars = [Car([200, 200], 3.14/4) for _ in range(10)]


running = True
def button_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
def update():
    for car in cars:
        car.update()
def draw():
    display.fill(BACKGROUND)
    for car in cars:
        car.draw(draw_tool, display)
    pygame.display.flip()



while running:
    button_events()
    update()
    draw()
    clock.tick(FPS)

pygame.quit()


