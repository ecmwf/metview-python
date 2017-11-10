# Build the docker image once with:
#   docker build -t mpy requirements
# Run the container with:
#   docker run --rm -it -v `pwd`:/src mpy
#
FROM ubuntu:16.04

# setup OS & Python
RUN apt-get -y update && apt-get install -y \
    build-essential \
    curl \
    git \
    liblapack-dev \
    libncurses-dev \
    libqt4-dev \
    python3-dev \
    python3-pip \
    python3-tk \
    python3-venv \
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
RUN cat /tmp/MetviewBundle-2017.10.90-Source.tar.gz \
    | tar -xzC /tmp \
    && mkdir /tmp/build \
    && cd /tmp/build \
    && cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF /tmp/MetviewBundle-2017.10.90-Source \
    && make -j 4 || make \
    && make install \
 && rm -rf /tmp/build /tmp/MetviewBundle*

# setup workdir
COPY requirements-tests.txt /

# setup the python and pytest environments
RUN pip3 install -r /requirements-tests.txt


WORKDIR /src
RUN echo "import setuptools as s; s.setup(name='package-to-test')" > setup.py \
 && pip3 install -e /src
