#Color wheels are cool

import math, colorsys

outFile = "output.ppm"
head = "P3"
dims = "500 500"
max = "255"
imgArray = []

def setupArray(imgArray,x,y):
    for i in range(x):
        imgArray.append([])
        for j in range(y):
            imgArray[i].append(["0","0","0"])

def dist(a,b,c,d):
    return math.pow(math.pow(a-c,2) + math.pow(b-d,2),.5)

def ang(x,y,a,b):
    if (x == a):
        if (y == b or y > b): #Point overlap or point directly above center
            return 90
        else: #Point directly below center
            return 270
    reflect = 0
    if x < a: reflect = 180 #Reflect if point is in quadrant II or III relative to center
    m = (y-b)/(x-a)
    output = (math.degrees(math.atan(m)) + reflect + 360) % 360 #Ensures positive
    return output

def getHue(x,y,a,b):
    angle = ang(x,y,a,b)
    return angle / 360

def writeFile(file):
    #Header
    lst = [head,dims,max]
    for i in lst:
        file.write(i + "\n")
    #Body
    split = dims.split()
    split[0] = int(split[0]) #Max X coordinate
    split[1] = int(split[1]) #Max Y coordinate
    maxRad = 220 #Wheel radius
    setupArray(imgArray,split[0],split[1])
    for y in range(split[1]):
        for x in range(split[0]):
            currDist = dist(split[0]/2,split[1]/2,x,y)
            if currDist > maxRad: #Color black if over the radius
                pass
            else:
                hsv = ( getHue(x,y,split[0]/2,split[1]/2),
                        currDist / maxRad,
                        1) #HSV value for x,y to the center
                red,green,blue = colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])
                dim = 1 #To be multiplied with color to make the transition from the color wheel to the background smoother
                if maxRad - currDist < 5:
                    dim = (maxRad - currDist) / 5
                imgArray[x][y][0] = str(int(red * 255 * dim))
                imgArray[x][y][1] = str(int(green * 255 * dim))
                imgArray[x][y][2] = str(int(blue * 255 * dim))
    for y in range(split[1]):
        for x in range(split[0]):
            for i in imgArray[x][y]:
                file.write(i + " ")
        file.write("\n")

outFile = open(outFile,'w')
writeFile(outFile)
