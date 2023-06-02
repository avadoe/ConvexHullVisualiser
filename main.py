import pygame
import color_values
import random

pygame.init()

WIDTH, HEIGHT = 750, 600
DELTA = 25
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
NUM_POINTS = 25
pygame.display.set_caption('Convex Hull Visualisation')
clock = pygame.time.Clock()

points = [(random.randint(DELTA, WIDTH - DELTA), random.randint(DELTA, HEIGHT - DELTA)) for _ in range(NUM_POINTS)]

def orientation(p, q, r):
    slope1 = (q[1] - p[1]) * (r[0] - q[0])
    slope2 = (r[1] - q[1]) * (q[0] - p[0])
    if slope1 == slope2: return 0 # collinear
    elif slope1 > slope2: return 1 # clockwise
    else: return 2 # anticlockwise
    
def convex_hull(points):
    n = len(points)
    
    if n < 3:
        return points
    
    hull_points = []
    
    l = 0
    for i in range(n):
        if points[i][0] < points[l][0]:
            l = i
            
    p = l
    q = 0
    
    while True:
        hull_points.append(points[p])
        q = (p + 1) % n
        
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i   
        p = q
        
        if p == l: break
        
    return hull_points

running = True
draw_line = False
line_index = 1
lines = []

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            pygame.quit()

    WINDOW.fill(color_values.WHITE)  
    
    for point in points:
        pygame.draw.circle(WINDOW, color_values.BLACK, point, 10)
        
    hull_points = convex_hull(points)
    
    if draw_line:
        lines.append((hull_points[line_index - 1], hull_points[line_index]))
        pygame.draw.line(WINDOW, color_values.BLACK, hull_points[line_index - 1], hull_points[line_index], 4)
        line_index += 1
        
        if line_index > len(hull_points):
            draw_line = False
            
    for line in lines:
        pygame.draw.line(WINDOW, color_values.BLACK, line[0], line[1], 4)
            
    if line_index <= len(hull_points):
        draw_line = True
    
    if line_index == len(hull_points):
        pygame.draw.line(WINDOW, color_values.BLACK, hull_points[line_index - 1], hull_points[0], width=4)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
    
    pygame.display.update()
    pygame.time.delay(1000)
    
pygame.quit()