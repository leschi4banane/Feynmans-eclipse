import pygame as pg, math

# sets up window
pg.init()
screen = pg.display.set_mode((801,801))
clock = pg.time.Clock()

# rotates a point around a center
def rotate_point(angle,px,py,cx,cy):
    return (math.cos(angle) * (px - cx) - math.sin(angle) * (py - cy) + cx, math.sin(angle) * (px - cx) + math.cos(angle) * (py - cy) + cy)
# creates option variables
start_point = (0,0)
number_points = 100

run = True
while run:
    # checks for user input
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                number_points += 100
            if event.key == pg.K_LEFT:
                if number_points != 0:
                    number_points -= 100
            pg.image.save(screen,"screenshot.png")
    # sets caption to the number of points
    pg.display.set_caption(f"points: {number_points}")
    # clears screen
    screen.fill((0,0,0))
    # sets and draws the start point to the mouse cursor position
    start_point = pg.mouse.get_pos()
    pg.draw.circle(screen,(0,0,0), start_point, 5)

    # draws the big circle
    pg.draw.circle(screen, (0,0,0), (401,401), 300, 1)

    # creates the evenly distributed on the circle
    point_list = []
    for i in range(number_points):
        angle = (math.pi*2 / number_points) * i
        x = 401 + round(math.cos(angle) * 300)
        y = 401 + round(math.sin(angle) * 300)
        point_list.append((x,y))

    # creates all the lines connecting the outer points with the inner point
    # rotates these lines and stores them in a list to draw them later (this is so the final lines are drawn over the other ones)
    rotated_lines = []
    for i in point_list:
        pg.draw.aaline(screen, (155,155,155), i, start_point)
        mp = ((start_point[0]+i[0])/2, (start_point[1]+i[1])/2)
        rotated_lines.append((rotate_point(math.radians(90), i[0], i[1], mp[0], mp[1],), rotate_point(math.radians(90), start_point[0], start_point[1], mp[0], mp[1])))

    # draws the rotated lines    
    for i in rotated_lines:
        pg.draw.aaline(screen, (171, 25, 250), i[0], i[1])

    # updates screen
    pg.display.flip()
    clock.tick(60)