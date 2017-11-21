# run tests in a more reproduceble and isolated environment
#
# Build the docker image once with:
#   docker build -t mpy-tox .
# Run the container with:
#   docker run --rm -it -v `pwd`:/src mpy-tox
#
FROM bopen/ubuntu-pyenv:latest

RUN apt-get -y update && apt-get -y build-dep --no-install-recommends \
    metview \
    magics++ \
    emoslib \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get -y update && apt-get install -y \
    libqt4-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements/source /tmp/source

RUN mkdir /tmp/build \
    && cd /tmp/build \
    && cmake -DENABLE_ODB=ON -DENABLE_XXHASH=OFF /tmp/source \
    && make -j 4 || make \
    && make install \
 && rm -rf /tmp/build /tmp/source

RUN pip3 install pip setuptools wheel tox==2.9.1 tox-pyenv==1.1.0

WORKDIR /src

ENTRYPOINT ["tox", "--workdir", ".docker-tox"]
