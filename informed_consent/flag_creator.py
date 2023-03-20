from PIL import Image, ImageDraw, ImageFont, ImageColor
import os, csv, random

flag_list = []
num_flag = 25

'''
generate RGB tuples for each possible flag
'''

'''
definitions
'''
def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

'''
generate num_flag random flags, each with 6 colors
'''

for i in range(1,num_flag + 1):
    flag = []
    for j in range(1,7):
        color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
        flag.append(color)
    flag_list.append(flag)

'''
generate pride flag
'''

flag_list.append([(255,0,24),(255,165,44),(255,255,65),(0,128,24),(0,0,249),(134,0,125)])
      

'''
define getSize to get the intended size of the text to be converted to a png file

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)
'''

    
'''
for each flag vector, create a png image
'''
os.chdir("/Users/chaddi/rpi_3208/_static/flag_survey/flags")

'''
staging area code
'''


for i in range(len(flag_list)):
    im = Image.new('RGB', (180,15),flag_list[i][0])
    for j in range(1,len(flag_list[i])):
        new_im = Image.new('RGB', (180,15),flag_list[i][j])
        im = get_concat_v(im, new_im)
    if i<50:
        im.save("flag_"+str(i+1)+".png")
    else:
        im.save("flag_"+str(num_flag + 1)+".png")


