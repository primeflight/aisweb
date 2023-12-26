import os
import glob
import json


class AISWEB:
    @staticmethod
    def abbreviations():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
        directory = os.path.join(project_root, "data/abbreviations/")
        files = glob.glob(os.path.join(directory, "*.json"))

        if files:
            latest_file = max(files, key=os.path.getctime)

            with open(latest_file, "r") as file:
                data = json.load(file)
                return data
        else:
            return None

    @staticmethod
    def broadcasters():
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

        directory = os.path.join(project_root, "data/broadcasters/")
        files = glob.glob(os.path.join(directory, "*.json"))

        if files:
            latest_file = max(files, key=os.path.getctime)

            with open(latest_file, "r") as file:
                data = json.load(file)
                return data
        else:
            return None
