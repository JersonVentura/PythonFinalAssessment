def sepia(oldPixel):
    red = oldPixel.getred()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()
    newred = 0.393*100 + 0.769*150 + 0.189*200
    newgreen = 0.349*100 + 0.686*150 + 0.168*200
    newblue =  0.272*100 + 0.534*150 + 0.131*200
    newPixel = Pixel(newred, newblue, newgreen)
    return newPixel
