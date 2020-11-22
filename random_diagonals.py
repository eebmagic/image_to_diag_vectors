import random

def draw_diagonal(x, y, x2, y2, color='black'):
    #format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" \
            y2="{y2}" stroke="{color}" />'


def make_lines(num, color = "black", height = 500):
    width = height
    step = height // num
    
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    print(header)

    for row in range(0, height, step):
        for col in range(0, width, step):
            pos = random.randint(0, 10)
            print(draw_diagonal(col, row, col+pos, row+pos))

    #write the footer
    footer = f'</svg>'
    print(footer)

if __name__ == "__main__":
    make_lines(50)