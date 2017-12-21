# Run tests in a more reproducible and isolated environment.
#
# Build the docker image once with:
#   docker build -t mpy-tox .
# Run the container with:
#   docker run --rm -it -v `pwd`:/src mpy-tox
#
FROM bopen/ubuntu-pyenv:latest

RUN apt-get -y update && apt-get -y install --no-install-recommends \
    curl \
    && apt-get -y build-dep --no-install-recommends \
    metview \
    magics++ \
    emoslib \
 && rm -rf /var/lib/apt/lists/*

RUN curl -SL https://software.ecmwf.int/wiki/download/attachments/51731119/MetviewBundle-2017.12.0-Source.tar.gz \
    | tar -xzC /tmp \
    && mkdir /tmp/build \
    && cd /tmp/build \
    && cmake -DENABLE_UI=OFF -DENABLE_ODB=ON -DENABLE_XXHASH=OFF /tmp/MetviewBundle-2017.12.0-Source \
    && make -j 4 \
    && make install \
 && rm -rf /tmp/*

RUN pip3 install pip setuptools wheel tox==2.9.1 tox-pyenv==1.1.0

WORKDIR /src

ENTRYPOINT ["tox", "--workdir", ".docker-tox"]
