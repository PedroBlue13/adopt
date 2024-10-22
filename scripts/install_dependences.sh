#!/bin/bash
chmod +x install_python.sh
#esse bloco atualiza os pacotes e instala dependências essenciais do linux
sudo apt update
sudo apt install -y software-properties-common
#add o rep do python mais recente
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
#aqui colocamos a versão desejada
sudo apt install -y python3.13 python3.13-venv python3.13-dev  
#configura a versão como padrao(opcional)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.13 1
#
python3.13 -m venv ~/dev_work/venv


echo "Python 3.13 instalado e ambiente virtual criado em ~/dev_work/venv"

cd  /home/ubuntu/dev_work
source /home/ubuntu/dev_work/bin/activate