# Import the required libraries
from torchvision.io import read_image
import time
import pygame.camera
import pygame
import os

os.chdir("/assets")
counter3 = 0
image = pygame.SurfaceType
slope = 1
start = 0


def check_captures():
    global counter3, slope, start
    if counter3 >= 100:
        start = time.time()

        img = read_image(("pic" + str(counter3) + ".jpg"))

        d = img.numpy()

        size_x = 128
        size_y = 72

        color1 = 0
        total = 0
        different = 0

        for a in range(0, (size_y - 1)):
            for b in range(0, (size_x - 1)):  # range(0, (x[2] - 1))
                color2 = color1
                color1 = 0.2989 * d[0][15 * a][15 * b] + 0.5870 * d[1][15 * a][15 * b] + 0.1140 * d[2][15 * a][15 * b]
                if color2 + 20 >= color1 >= color2 - 20:
                    total += 1
                else:
                    different += 1
                    total += 1

        slope = (slope * 1.1 + ((different/total)*10))/11

        if slope <= different/total:
            save_img_to_caught()


def capture_img_():
    pygame.camera.init(None)
    camlist = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(camlist[0], (1920, 1080), "rgb")
    cam.start()
    time.sleep(2)
    print("started")

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
    os.chdir("/caught")
    pygame.image.save(image, (str(timelist_[0]) + "__" + str(timelist_[1]) + "__" + str(timelist_[2]) + "__" +
                              str(timelist_[3]) + "_" + str(timelist_[4]) + "_" + str(timelist_[5]) + ".jpg"))
    os.chdir("/assets")
    print("time:", abs(time.time() - start))


capture_img_()
