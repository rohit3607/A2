import os
import platform
import shutil
import sys

class CheckDependencies:
    def __init__(self):
        self.is_pkg_installed()
        self.is_env()

    def is_pkg_installed(self):
        d = [
            shutil.which("ffmpeg"),
            shutil.which("aria2c"),
            shutil.which("mediainfo"),
            shutil.which("wget"),
        ]
        if not all(d):
            if platform.system() == "Linux":
                print("Dependecies Not Found !!")
                print(
                    "run 'sudo apt-get install git wget pv jq mediainfo gcc aria2 ffmpeg -y' to install dependencies to run this program"
                )
                sys.exit(1)
            if platform.system() == "Windows":
                print("Dependecies Not Found !!")
                print(
                    "Install Ffmpeg, Wget, Aria2c, Mediainfo Packages Into Environment Variable To run this program"
                )
                sys.exit(1)

    def is_env(self):
        if not os.path.exists(".env"):
            print("Unable To Find .env File")
            sys.exit(1)
