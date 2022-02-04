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


class LoremParser(DownloaderInterface, abc.ABC):
    url: str = 'https://loremflickr.com/'

    def __init__(self):
        super().__init__()
        self.counter = 1
        self.path = self.path
        self.resolution = "1080/720"

    def _parse_url(self) -> str:
        """The link consists of the name of the site and the resolution of the random picture you want to see."""
        return str(self.url + ''.join(self.resolution))

    async def get_image(self, name: str = "name"):
        image = self._parse_url()
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
    lp = LoremParser()
    asyncio.run(lp.get_images_collection())
    print("Need to execute from 'main.py'")
