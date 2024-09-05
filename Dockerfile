# Base image for Wine setup
FROM ubuntu:22.04

# Install Wine dependencies
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    software-properties-common \
    wine64 wine32 python3 python3-pip python3-dev git build-essential

# Install Python and PyInstaller
RUN python3 -m pip install --upgrade pip setuptools && \
    python3 -m pip install pyinstaller

# Set up working directory
WORKDIR /src

# Copy your Python script into the image
COPY . /src

# Build 64-bit Windows executable
RUN wine64 pyinstaller --noconfirm --onefile --console --distpath /output/win64 bot.py

# Set up Wine for 32-bit Windows
RUN WINEARCH=win32 WINEPREFIX=~/.wine32 wine pyinstaller --noconfirm --onefile --console --distpath /output/win32 bot.py

# Create output folder and set the command to list the output
CMD ["ls", "/output"]