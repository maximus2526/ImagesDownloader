import abc
import requests


class DownloaderInterface:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.path = "./pictures"

    @abc.abstractmethod
    def get_image(self):
        """Download obj"""

    @abc.abstractmethod
    def get_images_collection(self, count: int):
        """Get images collection"""


class LoremParser(DownloaderInterface, abc.ABC):
    url: str = 'https://loremflickr.com/'

    def __init__(self):
        super().__init__()
        self.counter = 1
        self.path = self.path

    def get_url(self, resolution: str = "1080/720") -> str:
        """The link consists of the name of the site and the resolution of the random picture you want to see."""
        return str(self.url + ''.join(resolution))

    def get_image(self, name: str = "name"):
        image = self.get_url()
        r = requests.get(image)
        with open(f"{self.path}/{name}.jpg", "wb") as file:
            file.write(r.content)

    def get_images_collection(self, count: int):
        while self.counter <= count:
            self.get_image(str(self.counter))
            self.counter += 1


if __name__ == "__main__":
    lp = LoremParser()
    lp.get_image()
    print("Need to execute from 'main.py'")
