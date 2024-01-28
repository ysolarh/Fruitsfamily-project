import os
import sys


class FileUtils:
    @classmethod
    def make_directories(cls, path) -> None:
        os.makedirs(cls.get_root_path() + path, exist_ok=True)

    @classmethod
    def find_by_path(cls, path) -> str:
        return cls.get_root_path() + path

    @classmethod
    def get_root_path(cls) -> str:
        return os.path.dirname(sys.modules["__main__"].__file__)
