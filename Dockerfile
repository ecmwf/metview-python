FROM ecmwf/jupyter-notebook:latest

ARG DEBIAN_FRONTEND="noninteractive"

ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"

COPY . /home/jovyan/work/
COPY .ecmwfapirc /home/jovyan/

USER root
RUN pip install -U pip \
    && pip install -r /home/jovyan/work/ci/requirements-tests.txt \
    && pip install matplotlib \
    && pip install -e /home/jovyan/work
