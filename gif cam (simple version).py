import picamera
from time import sleep
import time
from os import system
import os
import random, string


########################
#
# Behaviour Variables
#
########################
num_frame = 8       # Number of frames in Gif
gif_delay = 20 # Frame delay [ms]
rebound = True      # Create a video that loops start <=> end



camera = picamera.PiCamera()
camera.resolution = (540, 405)
camera.rotation = 90
camera.brightness = 60
camera.image_effect = 'none'


yes = input("type y")
print('System Ready')

def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



while True:
    if yes == ("y"): # Button Pressed
    
        ### TAKING PICTURES ###
        print('Gif Started')

        randomstring = random_generator()
        for i in range(num_frame):
            camera.capture('{0:04d}.jpg'.format(i))
            print(i)
                


        if rebound == True: # make copy of images in reverse order
            for i in range(num_frame - 1):
                source = str(num_frame - i - 1) + ".jpg"
                source = source.zfill(8) # pad with zeros
                dest = str(num_frame + i) + ".jpg"
                dest = dest.zfill(8) # pad with zeros
                copyCommand = "cp " + source + " " + dest
                os.system(copyCommand)
                
        filename = '/home/pi/Desktop/cam' + randomstring + '-0'
        print('Processing')

        graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " + filename + ".gif" 
        os.system(graphicsmagick)

        os.system("rm ./*.jpg") # cleanup source images


        print('Done')
        print('System Ready')
        break

    else : # Button NOT pressed
        ### READY TO MAKE GIF ###
        print("error")
        break
        
print("end")
