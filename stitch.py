import Image as img

im1 = img.open("./1.jpeg")
im2 = img.open("./2.jpeg")
im3 = img.open("./3.jpeg")

def width(image):
    return image[0]
    
def height(image):
    return image[1]

def imgToTuple(img):
    return img.size

def makeCanvas(images):
    y = max(map(height, images))
    x = sum(map(width, images))
    return img.new("RGB", (x , y))

def imappend(canvas, offset, im):
    canvas.paste(im, (offset, 0))
    return canvas

def concatImages(*ims):
    canvas = makeCanvas(map(imgToTuple, ims))
    offset = 0
    
    for im in ims:
        imappend(canvas, offset, im)
        offset += im.size[0]
    return canvas
    
concatImages(im1, im2, im3).show()