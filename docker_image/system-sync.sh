#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get -y upgrade
apt-get -y --no-install-recommends install sudo vim curl
apt-get -y --no-install-recommends install build-essential
apt-get -y --no-install-recommends install python3.5-dev python3-pip python3-venv python3-tk
apt-get -y build-dep metview
apt-get -y build-dep magics++
apt-get -y build-dep emoslib
apt-get -y --no-install-recommends install liblapack-dev libncurses-dev libqt4-dev git x11-utils xterm

python3 -m venv cpython3
./cpython3/bin/pip install -U setuptools pip wheel
