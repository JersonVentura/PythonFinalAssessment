def generalScale(oldimage, widthscale, heightscale):
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    newim = EmptyImage(oldw*widthscale,oldh*heightscale)
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            original col=col//widthscale
            originalrow=row//heightscale
            oldpixel=oldimage.getPixel(OriginalCol,originalRow)
            newim.setPixel(col,row,oldpixel)
        return newim
