height = 5
width = 5
background_color = 255

def fill_image(height, width, background_color):
    image = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(background_color)
        image.append(row)
    return image

image = fill_image(height, width, background_color)
for i in range(3):
    image[2][i + 1] = 0
    image[i + 1][2] = 0

file = "test.pgm"
with open(file, "w") as f:
    f.write("P2\n")
    f.write(f"{width} {height}\n")
    f.write(f"{background_color}\n")

    for row in image:
        f.write(" ".join(map(str, row)) + "\n")