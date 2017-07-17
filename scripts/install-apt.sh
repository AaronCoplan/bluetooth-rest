#!/usr/bin/bash

sudo -H pip install --upgrade pip

sudo apt install -y bluetooth
sudo apt install -y libbluetooth-dev
sudo apt install -y pkg-config
sudo apt install -y libboost-python-dev
sudo apt install -y libboost-thread-dev
sudo apt install -y libglib2.0-dev
sudo apt install -y python-dev

sudo apt update -y
sudo apt upgrade -y
sudo apt autoremove -y

sudo -H pip install gattlib
sudo -H pip install pybluez

sudo -H pip install flask
