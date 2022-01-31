from abc import abstractmethod


class DownloaderInterface:
    @abstractmethod
    def get_image(self):
        """Download obj"""

    @abstractmethod
    def get_images_collection(self):
        """Get images collection"""

    @abstractmethod
    def get_path(self):
        """Input path where image will be saved"""
