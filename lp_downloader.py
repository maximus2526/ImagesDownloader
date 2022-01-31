from abc import ABC
from os import mkdir

import requests
from typing import Tuple

from interface import DownloaderInterface


class LoremParser(DownloaderInterface, ABC):
    url: str = 'https://loremflickr.com/'

    def get_path(self, path: str = "./pictures"):
        return path

    def get_url(self, resolution: Tuple[str] = ("1080", "720")):
        """The link consists of the name of the site and the resolution of the random picture you want to see."""
        return str(self.url + '/'.join(resolution))

    def get_image(self, name: str = "name"):
        image = self.get_url()
        path = self.get_path()
        r = requests.get(image)
        with open(f"{path}/{name}.jpg", "wb") as file:
            file.write(r.content)


if __name__ == "__main__":
    print("Need to execute 'main.py'")
