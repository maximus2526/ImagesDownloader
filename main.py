from os import mkdir
from lp_downloader import LoremParser
import asyncio

parser = LoremParser()  # Create instance

# Terminal UI
have_many = int(input("How many images are you want?\n"))
choice_resolution = input("Hi! Images standard resolution = 1080/720. You want to change? (Y/N):\n")

if choice_resolution == ("Y" or "y" or "Yes" or "Да"):
    resolution = input("Input resolution of images like that '720/480':\n")
    parser.get_url(resolution)

choice_path = input("Change path:  (Y/N)\n")
if choice_path == ("Y" or "y" or "Yes" or "Да"):
    path = input("'./pictures' (Standard directory); Input path your path:\n")
    mkdir(path)
    parser.path = path

asyncio.run(parser.get_images_collection(int(have_many)))

print("Done.")
