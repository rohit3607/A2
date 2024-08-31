# Base image for 64-bit compilation
FROM ubuntu:22.04 as linux64-build

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3-pip gcc

# Install nuitka
RUN pip3 install nuitka

# Set the working directory in the container
WORKDIR /src

# Copy the source code into the container
COPY . /src

# Compile the Python script for 64-bit
RUN nuitka --standalone --onefile --output-dir=/output/linux64 "./bot.py"

# Base image for 32-bit compilation
FROM i386/ubuntu:22.04 as linux32-build

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3-pip gcc

# Install nuitka
RUN pip3 install nuitka

# Set the working directory in the container
WORKDIR /src

# Copy the source code into the container
COPY . /src

# Compile the Python script for 32-bit
RUN nuitka --standalone --onefile --output-dir=/output/linux32 "./bot.py"

# Combine all outputs
FROM busybox as final
COPY --from=linux64-build /output/linux64 /dist/linux64
COPY --from=linux32-build /output/linux32 /dist/linux32