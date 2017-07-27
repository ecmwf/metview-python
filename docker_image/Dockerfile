# Build the docker image once with:
#   docker build -t mpy mpy/docker_image
# Run a shell inside the container with:
#   open -a XQuartz
#   ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
#   xhost + $ip
#   docker run --rm -it -e DISPLAY=$ip:0 -v `pwd`:/src mpy bash
#
FROM ubuntu:16.04

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

WORKDIR /root

COPY system-sync.sh /root/
RUN /root/system-sync.sh
