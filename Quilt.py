from PIL import Image, ImageDraw
import sys

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
                scales.append(parts[0])
                red.append(parts[1])
                green.append(parts[2])
                blue.append(parts[3])

        im = Image.new('RGB', (500, 500), (255, 255, 255))
        draw = ImageDraw.Draw(im)




        im.save("curr.png")

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