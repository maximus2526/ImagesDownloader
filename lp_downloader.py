import abc
import asyncio
from time import time
import aiohttp


class DownloaderInterface:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.path = "./pictures"

    @abc.abstractmethod
    async def get_image(self):
        """Download obj"""

    @abc.abstractmethod
    async def get_images_collection(self):
        """Get images collection"""


# def check_time():  # Почему я не могу юзать это на методах класа?
#     def wrapper():
#         time_now = time()
#         func()
#         time_past = time()
#         time_past -= time_now
#         print(time_past)
#
#     return wrapper


class LoremParser(DownloaderInterface, abc.ABC):
    url: str = 'https://loremflickr.com/'

    def __init__(self):
        super().__init__()
        self.counter = 1
        self.path = self.path

    def get_url(self, resolution: str = "1080/720") -> str:
        """The link consists of the name of the site and the resolution of the random picture you want to see."""
        return str(self.url + ''.join(resolution))

    async def get_image(self, name: str = "name"):
        image = self.get_url()
        async with aiohttp.ClientSession() as session:
            async with session.get(url=image, allow_redirects=True) as response:
                content = await response.read()
        with open(f"{self.path}/{name}.jpg", "wb") as file:
            file.write(content)

    async def get_images_collection(self, count: int = 1):
        tasks = []
        for i in range(count):
            task = asyncio.create_task(self.get_image(name=str(i)))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    time_start = time()
    lp = LoremParser()
    asyncio.run(lp.get_images_collection())
    print("Time execution: {} sec".format(str(round(time() - time_start, 3))))
    print("Need to execute from 'main.py'")
