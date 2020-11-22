from PIL import Image
import numpy as np
import cv2

def find_next_nonwhite(startx, starty, matr, ignore):
    x = 0
    y = 0
    while matr[starty + y][startx + x] != ignore:
        x += 1
        y += 1

    return (startx + x - 1, starty + y - 1)

def find_last_match(startx, starty, matr):
    x = 0
    y = 0
    origin_color = matr[starty][startx]

    try:
        while matr[starty + y][startx + x] == origin_color:
            x += 1
            y += 1
    except IndexError:
        x -= 1
        y -=1

    return (startx + x - 1, starty + y - 1)


def draw_diagonal(x, y, x2, y2, color='black'):
    #format a line for svg 
    if type(color) == str:
        return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{color}" />'
    else:
        return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" style="stroke:rgb{str((255-color[0], 255-color[1], 255-color[2]))}" />'


def make_lines(matr, colors, step, color = "black", height = 500, width = 500):
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)

    back = matr[0][0]
    for y in range(0, len(matr), step):
        for x in range(0, len(matr[0]), step):
            if matr[y][x] != back:
                nextPoint = find_last_match(x, y, matr)
                if nextPoint != (x, y):
                    print(draw_diagonal(x, y, nextPoint[0], nextPoint[1], color=colors[y][x]))

    #write the footer
    footer = f'</svg>'
    print(footer)



## load image with cv2
image_PATH = "sources/Solar_System.jpg"
resize_dimension = (1920, 1080)
color = cv2.imread(image_PATH)
color = cv2.resize(color, resize_dimension)

img = cv2.imread(image_PATH, 0)
img = cv2.resize(img, resize_dimension)
# print(img)
# cv2.imshow("test", img)
# cv2.waitKey(0)

## make svg
make_lines(img, color, 5, color="black", height=resize_dimension[1], width=resize_dimension[0])