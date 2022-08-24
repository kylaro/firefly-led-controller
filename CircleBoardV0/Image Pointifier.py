import PIL
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

resolution=100 #pixels per linear inch
width=10 #in Inches
height=11.11 #in Inches

def ConvertPixelToX(nPixel,res, width):
    PixPerRow=width*res
    x=((nPixel%PixPerRow)/(width*res))*width
    return x
def ConvertPixelToY(nPixel,res, height):
    PixPerCollum=height*res
    y=((nPixel%PixPerCollum)/(height*res))*height
    return y


im=Image.open("LEDFormerTestCompressed.jpg")
#im.show()
pixels=np.array(im)
npixelsy=int(height*resolution)
npixelsx=int(width*resolution)
print(npixelsy)
print(npixelsx)
pi=[]
pj=[]
for i in range(0, npixelsy):
    for j in range(0, npixelsx):
        if (pixels[i,j] ==[255,255,255]).all():
            pixels[i,j]=[j%255, i%255,  150]
            if len(pi)==0:
                pi.append(i)
                pj.append(j)
                print("added to pi")
            if len(pi)>0:
                dist_check = True
                for s in range(len(pi)):
                    if(abs(i-pi[s]) < 40 and abs(j-pj[s]) < 80):
                        dist_check = False
                if dist_check:
                    pi.append(i)
                    pj.append(j)
            print("Found white at:" + str(ConvertPixelToX(i, resolution, width)) +', ' +str(ConvertPixelToY(j, resolution, height)))

print(pi)
print(pj)
print(len(pj))
plt.scatter(pj,pi)
plt.show()
Newim=Image.fromarray(pixels, mode="RGB")
#Newim.show()
Newim.save("outNew.png","PNG")

# newImg1 = Image.new('RGB', (20, 20))
# pixelsTwo=np.array(newImg1.getdata())
# print(pixelsTwo)
# print(len(pixelsTwo))
# pixelsTwo[range(0, 200)] = [0, 155, 0]
# print(pixelsTwo)
# bwnewImg2=Image.fromarray(pixelsTwo, mode="RGB")
# newImg2=bwnewImg2.convert('RGB')
# newImg2.save("TestOutTwo.png", "PNG")
# newImg1.save("TestOut.png","PNG")