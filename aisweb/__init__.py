import os
import glob
import json


class AISWEB:
    @staticmethod
    def abbreviations():
        directory = "data/abbreviations/"
        files = glob.glob(os.path.join(directory, "*.json"))

        if files:
            latest_file = max(files, key=os.path.getctime)

            with open(latest_file, "r") as file:
                data = json.load(file)
                return data
        else:
            return None
