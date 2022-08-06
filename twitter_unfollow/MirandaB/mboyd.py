import os
import json
import pathlib as plib
from loguru import logger, logger as log


def main():
    # dir_items =
    # resulting = os.path.join(f"file/location/sofar", "layers", "layerz", "lay")
    # logger.warning(resulting)

    # f"file/location/sofar/layers"
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
    x = sum([100, 200, 300])
    log.critical(x)


if __name__ == "__main__":
    main()
