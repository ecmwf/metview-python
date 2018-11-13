FROM ecmwf/jupyter-notebook:latest

ARG DEBIAN_FRONTEND="noninteractive"

ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"

USER root
COPY . /src
RUN pip install -r /src/ci/requirements-tests.txt \
    pip install -e .

USER jovyan
