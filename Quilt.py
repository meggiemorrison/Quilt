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
        a = 200
        b = 300
        c = 300
        d = 200
        sq_num = 1
        curr_num = 0
        #draw.rectangle((200, 300, 300, 200), fill=(255, 0, 0))
        for i in range(len(values)):
            drawRec(scales[i], red[i], green[i], blue[i], a, b, c, d, sq_num, curr_num, im)
            sq_num += 1


        im.save("curr.png")

# Pass in x and y as 100, 200
# square_num = 1
# curr_num = 0
def drawRec(scale, r, g, b, x1, y1, x2, y2, square_num, curr_num, im):
    base = 10000 * scale
    print(base)
    length = math.sqrt(base)
    half_length = length/2
    print(half_length)
    draw = ImageDraw.Draw(im)

    if curr_num == 4*square_num: # should we do if curr_num > 4*square num? will it draw the final round?
        return
    else:
        draw.rectangle((x1, y1, x2, y2), fill=(r, g, b))
    
    # Top left
    drawRec(scale, r, g, b, (x1 - half_length), (y1 + half_length), (x1 + half_length), (y1 - half_length), square_num, curr_num+4, im)
    # Bottom left
    drawRec(scale, r, g, b, (x1 - half_length), (y2 + half_length), (x1 + half_length), (y2 - half_length), square_num, curr_num+4, im)
    # Top right
    drawRec(scale, r, g, b, (x2 - half_length), (y1 + half_length), (x2 + half_length), (y1 - half_length), square_num, curr_num+4, im)
    # Bottom right
    drawRec(scale, r, g, b, (x2 - half_length), (y2 + half_length), (x2 + half_length), (y2 - half_length), square_num, curr_num+4, im)

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


# could call draw rec once, and then recursively call each time sending it a different
# corner in relation to x, y ????