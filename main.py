# Import the required libraries
from torchvision.io import read_image
import time
import pygame.camera
import pygame
import os

os.chdir("D:/Coding Projects/stayoutofmyroom/assets")
list_of_files = os.listdir()
for m in range(0, len(list_of_files)-1):
    os.remove(list_of_files[m])
counter3 = 0
image = pygame.SurfaceType
slope = []


def check_captures():
    global counter3, slope
    if counter3 >= 1:

        counter = 0
        counter2 = 0

        img = read_image(("pic" + str(counter3) + ".jpg"))
        img2 = read_image(("pic" + str(counter3 - 1) + ".jpg"))

        d = img.numpy()
        c = img2.numpy()

        size_x = 128
        size_y = 72

        for a in range(0, (size_y - 1)):
            for b in range(0, (size_x - 1)):  # range(0, (x[2] - 1))
                if (c[0][15 * a][15 * b] + 10 >= d[0][15 * a][15 * b] <= c[0][15 * a][15 * b] - 10) and \
                        (c[1][15 * a][15 * b] + 10 >= d[1][15 * a][15 * b] <= c[1][15 * a][15 * b] - 10) and \
                        (c[2][15 * a][15 * b] + 10 >= d[2][15 * a][15 * b] <= c[2][15 * a][15 * b] - 10):
                    pass
                else:
                    counter += 1
                counter2 += 1
                #  print(c[0][6 * a][6 * b], d[0][6 * a][6 * b])

        e = counter/counter2

        #  print(e)

        os.remove(("pic" + str(counter3 - 1) + ".jpg"))

        if len(slope) == 6:
            del slope[0]
            slope.append(e)
        else:
            slope.append(e)

        slope2 = (sum(slope)/len(slope)) - 0.005

        # print("slope2:", slope2)

        if e < slope2 and counter3 != 3:
            save_img_to_caught()

        return e
    else:
        return "none"


def capture_img_():
    print("started")
    pygame.camera.init(None)
    camlist = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(camlist[0], (1920, 1080), "rgb")
    cam.start()

    while True:
        global counter3, image

        image = cam.get_image()

        pygame.image.save(image, ("pic" + str(counter3) + ".jpg"))
        check_captures()

        counter3 += 1


def save_img_to_caught():
    if counter3 <= 7:
        return
    print("caught")
    timelist_ = time.localtime()
    os.chdir("D:/Coding Projects/stayoutofmyroom/caught")
    pygame.image.save(image, (str(timelist_[0]) + "__" + str(timelist_[1]) + "__" + str(timelist_[2]) + "__" +
                              str(timelist_[3]) + "_" + str(timelist_[4]) + "_" + str(timelist_[5]) + ".jpg"))
    name = f"{timelist_[0]}__{str(timelist_[1])}__{str(timelist_[2])}__{str(timelist_[3])}_{str(timelist_[4])}_{str(timelist_[5])}.jpg"
    os.chdir("D:/Coding Projects/stayoutofmyroom/assets")


time.sleep(10)
capture_img_()
