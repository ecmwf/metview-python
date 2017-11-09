# Build the docker image once with:
#   docker build -t mpy docker_image
# Run a shell inside the container with:
#   open -a XQuartz
#   ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
#   xhost + $ip
#   docker run --rm -it -e DISPLAY=$ip:0 -v `pwd`:/src mpy bash
#
FROM ubuntu:16.04

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    liblapack-dev \
    libncurses-dev \
    libqt4-dev \
    python3-pip \
    python3-tk \
    python3-venv \
    python3.5-dev \
    sudo \
    vim \
    x11-utils \
    xterm

RUN apt-get -y build-dep \
    metview \
    magics++ \
    emoslib \
 && rm -rf /var/lib/apt/lists/*

COPY MetviewBundle-2017.10.90-Source.tar.gz /tmp/
RUN tar -xzf /tmp/MetviewBundle-2017.10.90-Source.tar.gz -C /tmp \
    && mkdir /tmp/MetviewBundle-2017.10.90-Build \
    && cd /tmp/MetviewBundle-2017.10.90-Build \
    && cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF /tmp/MetviewBundle-2017.10.90-Source \
    && make -j 4 \
    && ctest /tmp/MetviewBundle-2017.10.90-Source/metview \
    && make install \
    && ldconfig /usr/local/lib \
 && rm -rf /tmp/MetviewBundle*

WORKDIR /src
RUN echo "import setuptools as s; s.setup(name='package-to-test')" > setup.py \
 && pip3 install -e /src
