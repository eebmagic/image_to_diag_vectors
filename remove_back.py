from PIL import Image
from tqdm import tqdm

def compare(pointA, pointB):
    total = 0
    for i in range(min(len(pointA), len(pointB))):
        total += abs(pointA[i] - pointB[i])
    return total

## Load image
image_PATH = "lines.PNG"
im = Image.open(image_PATH).convert("RGB")
data = list(im.getdata())

red_back = data[0]  ## background color to ignore
# print(len(data))
# print(im.size)
# print(data[:30])

## form new data without red background color
newdata = []
for point in tqdm(data):
    if compare(point, red_back) <= 80:
        newdata.append((255, 255, 255))
    else:
        newdata.append(point)

## make new Image from new data
new = Image.new("RGB", size=im.size)
new.putdata(newdata)
new.save("output.png")