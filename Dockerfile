# Run tests in a more reproducible and isolated environment.
#
# Build the docker image once with:
#   docker build -t metview .
# Run the container with:
#   docker run --rm -it -v `pwd`:/src metview
#
FROM bopen/ubuntu-pyenv:latest

ARG SOURCE="MetviewBundle-2018.10.0-Source.tar.gz"
ARG CMAKEFLAGS="-DENABLE_UI=OFF -DENABLE_EXPOSE_SUBPACKAGES=ON -DENABLE_ODB=ON -DENABLE_PYTHON=ON"
ARG DEBIAN_FRONTEND="noninteractive"

ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"

RUN apt-get -y update && apt-get install -y --no-install-recommends \
    bison \
    cmake \
    curl \
    flex \
    gfortran \
    netbase \
    libboost-dev \
    libfreetype6-dev \
    libfftw3-dev \
    libgdbm-dev \
    libopenjp2-7-dev \
    libpango1.0-dev \
    libproj-dev \
    libnetcdf-cxx-legacy-dev \
    libnetcdf-dev \
    libpng-dev \
    libxml-parser-perl \
    pkg-config \
    swig \
 && rm -rf /var/lib/apt/lists/*

COPY $SOURCE /tmp/$SOURCE

RUN cd /tmp \
    && pyenv local 2.7.15 && pip install numpy jinja2 \
    && mkdir /tmp/source \
    && tar -xz -C /tmp/source --strip-components=1 -f /tmp/$SOURCE \
    && mkdir /tmp/build \
    && cd /tmp/build \
    && cmake $CMAKEFLAGS /tmp/source \
    && make -j 4 ; make \
    && make -j 4 install \
    && ldconfig /usr/local/lib \
 && rm -rf /tmp/*

COPY . /src/

RUN cd /src \
    && make local-install-test-req \
    && make local-develop \
    && make local-install-dev-req \
    && make cacheclean \
 && rm -rf /src/*

EXPOSE 8888
VOLUME /src
WORKDIR /src
