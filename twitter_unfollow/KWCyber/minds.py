from asyncio.log import logger
from ctypes import sizeof
from email.mime import image
import pathlib
import json
from terminaltables import AsciiTable

BASE_DIR = pathlib.Path(__file__).parent


class ImageTable:
    
    def __init__(self, *args, **kwargs):
        pass
        # print(args)
        # print(kwargs)

    def table_images(self):
        images = [
            ["name", "version", "size", "file"]
        ]  # what does file mean here? == the json file
            # this list is a header

        for file in BASE_DIR.iterdir():
            print(f"'{file.name}' is the file's name")
            # print(file.exists())
            # print(file.suffix)
            # print(file.name.endswith(".json"))
            # print("\n")

            if file.name.endswith(".json"):
                # print(file.read_text()) 
                # This is a dictionary: Because json.loads is a command that takes in a string or byte array and converts it to text
                image = json.loads(file.read_text())
                # with open(pathlib.path.join(BASE_DIR, image), 'r') as json_f:
                # image = json.loads(json_f.read())
                image_base = BASE_DIR
            print(f"'{sizeof.file}' is the file size")
            
        return images


# print(BASE_DIR)
# print(__file__)
# print(pathlib.Path.parent)

def run(self):
    images = self.table_images()
    table = AsciiTable(images)
    print(table.table)
