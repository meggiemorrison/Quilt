from PIL import Image, ImageDraw
import sys
import math

values = []
value_count = 0
scales = []
red = []
green = []
blue = []

def main():
    if __name__ == "__main__":
        global values
        global scales
        global red
        global green
        global blue

        fill_values()

        for line in values:
            parts = line.split()
            if len(parts) == 4:
                scales.append(float(parts[0]))
                red.append(int(parts[1]))
                green.append(int(parts[2]))
                blue.append(int(parts[3]))

        im = Image.new('RGB', (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(im)


        queue = [(0, 250, 250, 200)]
        drawRec2(queue, im)


        im.save("curr.png")


def drawRec2(queue, im):
    global scales
    global red
    global green
    global blue
    draw = ImageDraw.Draw(im)

    if(not queue):
        return

    current = queue.pop(0)  
    # current = (depth, x, y, side_length)
    depth, x, y, side_length = current

    if (depth >= len(scales)):
        return

    side_length = side_length * scales[depth]
    draw.rectangle((x-side_length/2, y-side_length/2, x+side_length/2, y+side_length/2),
                    fill=(red[depth], green[depth], blue[depth]))
    
    # Top left
    queue.append((depth + 1, x-side_length/2, y+side_length/2, side_length))
    # Bottom left
    queue.append((depth + 1, x-side_length/2, y-side_length/2, side_length))
    # Top right
    queue.append((depth + 1, x+side_length/2, y+side_length/2, side_length))
    # Bottom right
    queue.append((depth + 1, x+side_length/2, y-side_length/2, side_length))

    drawRec2(queue, im)

# Reads from stdin and adds input to a list
def fill_values():  
    global values
    global value_count  
    for line in nonblank_lines(sys.stdin):
        line = line.rstrip("\r\n")
        values.append(line) 
        value_count += 1

# Ignores blank lines provided in input
# https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python 
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

# Driver code:

main()
