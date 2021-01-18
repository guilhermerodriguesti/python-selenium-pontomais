#!/bin/bash

function install() {
    echo "INSTALL PYTHON REQUIREMENTS"
    pip3 install -r requirements.txt
}

function ponto() {
    echo "REGISTER"
    python3 ponto.py
}
function mail() {
    echo "EMAIL SEND"
    python3 mail.py
}
install
#ponto
mail