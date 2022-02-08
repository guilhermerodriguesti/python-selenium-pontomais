#!/bin/bash

function install() {
    echo "INSTALL PYTHON REQUIREMENTS ON MAC"
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    python3 --version
    pip3 --version
    pip3 install selenium
    brew install chromedrive

}

function ponto() {
    echo "REGISTER"
    touch .env
    echo 'USUARIO="mudar-no@env.com"' > .env
    echo 'SENHA="pass"' >> .env
    python3 ponto.py
}
function mail() {
    echo "EMAIL SEND"
    python3 mail.py
}
install
ponto
#mail