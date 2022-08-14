#1.) What is an image?-The Image module provides a class with the same name which is used to represent a PIL image. 
#2.) What is a JSON file?-JSON (JavaScript Object Notation) is a data format used for representing structured data
#3.) How do I open a json file?-Users can open the JSON file in any text editor as it is a plain text-based file.
#4.)How do I read json?-By using the  loads()(str) and load()(file) methods are gonna help us to read the JSON file.
#5.)How to do important things with json data? JSON allows you to gather data from a source, extracting useful 
# information, and passing that information along or keeping a record of it.

import os
import json
import pathlib as plib
#import sys
#from tabulate import tabulate
from loguru import logger, logger as log


def main():
    dir_items = resulting = os.path.join(f"file/location/sofar", "imgs", "test", "twitter_unfollow")
    log.warning(resulting)

    f"file/location/sofar/layers"
    for image_file in os.listdir("."):
        if image_file.endswith(".json"):
            with open(image_file) as f:
                data = json.load(f)
                logger.info(data["name"])
            log.warning(image_file)
            log.success(image_file.replace(".json", ""))
            image_base = os.path.join(".", image_file.replace(".json", ""), "layers")
            for os_file in os.listdir(image_base):
                log.debug(os_file)
                if os.path.isfile(os.path.join(image_base, os_file)):
                    log.success(os_file)

            log.info(image_base)
            log.error(image_base)
    x = sum([100, 200, 300, 400])
    log.critical(x)


if __name__ == "__main__":
    main()

