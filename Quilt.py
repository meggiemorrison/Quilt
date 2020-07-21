from PIL import Image, ImageDraw, ImageOps
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
            
        j = set_side(scales)
        base = (j/2) * (j/2)
        #print(base)
        x = 500
        y = 500

        im = Image.new('RGBA', (x, y), (255, 255, 255))

        queue = [(0, (x/2), (y/2), j)]
        drawRec2(queue, im, j)

        im.save("curr.png")


def drawRec2(queue, im, j):
    global scales
    global red
    global green
    global blue
    draw = ImageDraw.Draw(im)
    
    if(not queue):
        return

    current = queue.pop(0)  
    depth, x, y, side_length = current

    if (depth >= len(scales)):
        return

    print("og side_length: ", side_length)
    side_length = scales[depth] * j
    print ("new side length", side_length, "\nscale: ", scales[depth])
    draw.rectangle((x-side_length/2, y-side_length/2, x+side_length/2, y+side_length/2),
                    fill=(red[depth], green[depth], blue[depth]))

    # Top left
    queue.append((depth + 1, x-side_length/2, y+side_length/2, j))
    # Bottom left
    queue.append((depth + 1, x-side_length/2, y-side_length/2, j))
    # Top right
    queue.append((depth + 1, x+side_length/2, y+side_length/2, j))
    # Bottom right
    queue.append((depth + 1, x+side_length/2, y-side_length/2, j))

    drawRec2(queue, im, j)

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

def set_side(nums):
    big = []
    small = []
    for val in nums:
        if val > 0.5:
            big.append(val)
        else:
            small.append(val)
    
    max_sc = max(float(sub) for sub in nums) 
    if max_sc >= 2.0:
        j = 80
    elif max_sc > 1.0:
        j = 125
    elif len(big) > 2:
        j = 180
    else:
        j = 250
    return j

# Driver code:

main()
