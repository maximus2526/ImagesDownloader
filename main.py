from os import mkdir

from lp_downloader import LoremParser

# Terminal UI

photo = LoremParser()

have_many = int(input("How many images are you want?\n"))

choice_resolution = input("Hi! Images standard resolution = 1080/720. You want to change? (Y/N):\n")
if choice_resolution == ("Y" or "y" or "Yes" or "Да"):
    resolution = tuple(input("Input resolution of images like that '720,480':\n"))
    photo.get_url(resolution)

choice_path = input("Change path:  (Y/N)\n")
if choice_path == ("Y" or "y" or "Yes" or "Да"):
    path = input("'./pictures' (Standard directory); Input path your path:\n")
    mkdir(path)
    photo.get_path(path)

counter = 1
while counter != have_many:
    photo.get_image(str(counter))
    counter += 1