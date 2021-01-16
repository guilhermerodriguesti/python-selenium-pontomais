#!/bin/bash

function install() {
    echo "INSTALL PYTHON REQUIREMENTS"
    pip3 install -r requirements.txt
}

function ponto() {
    echo "REGISTER PONTO"
    python3 ponto.py
}
install
ponto