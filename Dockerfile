# Run tests in a more reproducible and isolated environment.
#
# Build the docker image once with:
#   docker build -t mpy .
# Run the container with:
#   docker run --rm -it -v `pwd`:/src mpy
#
FROM bopen/ubuntu-pyenv:latest

ARG SOURCE=MetviewBundle-2017.12.1-Source.tar.gz

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

RUN apt-get -y update && apt-get -y build-dep --no-install-recommends \
    metview \
    magics++ \
    emoslib \
 && rm -rf /var/lib/apt/lists/*

COPY $SOURCE /src/$SOURCE

RUN cd /tmp \
    && pyenv local 2.7.14 && pip install jinja2 \
    && mkdir /tmp/source \
    && tar -xz -C /tmp/source --strip-components=1 -f /src/$SOURCE \
    && mkdir /tmp/build \
    && cd /tmp/build \
    && cmake -DENABLE_UI=OFF -DENABLE_EXPOSE_SUBPACKAGES=ON ENABLE_ODB=ON /tmp/source \
    && make -j 4 ; make \
    && make install \
    && ldconfig /usr/local/lib \
 && rm -rf /tmp/*

COPY . /src/

RUN cd /src \
    && make local-install-test-req \
    && make local-develop \
    && make local-install-dev-req \
 && rm -rf /src/*

EXPOSE 8888
VOLUME /src
WORKDIR /src
