import math

outFile = "output.ppm"
head = "P3"
dims = "500 500"
max = "255"

def dist(a,b,c,d):
    return math.pow(math.pow(a-c,2) + math.pow(b-d,2),.5)

def writeFile(file):
    #Header
    lst = [head,dims,max]
    for i in lst:
        file.write(i + "\n")
    #Body
    split = dims.split()
    split[0] = int(split[0])
    split[1] = int(split[1])
    maxDist = int(dist(0,0,split[0],split[1]))
    for i in range(split[1]):
        for j in range(split[0]):
            red = 255 * j // split[0]
            green = 255 * dist(0,0,j,i) // maxDist
            blue = 255 * i // split[1]
            file.write(str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + " ")
        file.write("\n")

outFile = open(outFile,'w')
writeFile(outFile)
