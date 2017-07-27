#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive

apt-get update && apt-get -y upgrade
apt-get -y --no-install-recommends install sudo vim curl
apt-get -y --no-install-recommends install build-essential python3.5-dev python3-pip python3-venv
apt-get -y build-dep metview
apt-get -y build-dep magics++
apt-get -y build-dep emoslib
apt-get -y --no-install-recommends install liblapack-dev libncurses-dev libqt4-dev git x11-utils libffi-dev

python3 -m venv cpython3
