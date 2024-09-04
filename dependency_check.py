import os
import platform
import shutil
import sys
import requests

class CheckDependencies:
    def __init__(self):
        self.is_pkg_installed()
        self.is_env()
        self.is_assest()

    def is_pkg_installed(self):
        d = [
            shutil.which("ffmpeg"),
            shutil.which("aria2c"),
            shutil.which("mediainfo")
        ]
        if not all(d):
            if platform.system() == "Linux":
                print("Dependecies Not Found !!")
                print(
                    "run 'sudo apt-get install git pv jq mediainfo gcc aria2 ffmpeg -y' to install dependencies to run this program"
                )
                sys.exit(1)
            if platform.system() == "Windows":
                print("Dependecies Not Found !!")
                print(
                    "Install Ffmpeg, Aria2c, Mediainfo Packages Into Environment Variable To run this program"
                )
                sys.exit(1)

    def is_env(self):
        if not os.path.exists(".env"):
            print("Unable To Find .env File")
            sys.exit(1)

    def is_assest(self):
        if not os.path.isdir("assest/"):
            os.mkdir("assest/")
        if not os.path.exists("assest/poster_not_found.jpg"):
            content = requests.get("https://raw.githubusercontent.com/kaif-00z/AutoAnimeBot/main/assest/poster_not_found.jpg").content
            with open("assest/poster_not_found.jpg", "wb") as f:
                f.write(content)
