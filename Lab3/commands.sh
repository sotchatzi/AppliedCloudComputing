#git clone https://github.com/sotchatzi/AppliedCloudComputing.git
#cd Lab3
#commands.txt
# scp -i <key> data.tar.gz ubuntu@<ip>:/home/ubuntu
#!/bin/bash  


echo "#vim to terminal" >> /home/ubuntu/.bashrc
echo "set -o vi" >> /home/ubuntu/.bashrc
source /home/ubuntu/.bashrc

sudo apt update
echo ""
echo "Update done!"
echo ""

sudo apt -y upgrade
echo ""
echo "Upgrade done!"
echo ""

sudo apt install -y python-minimal
echo ""
echo "python minimal installed!"
echo ""

sudo apt install -y python-pip
echo ""
echo "python pip installed!"
echo ""

sudo apt install -y python3-pip
echo ""
echo "python pip3 installed!"
echo ""

sudo tar xvzf data.tar.gz
echo ""
echo "export data.tar.gz!"
echo ""

sudo apt-get install -y rabbitmq-server
echo ""
echo "install rabbitmq-server!"
echo ""

pip install celery
echo ""
echo "install celery!"
echo ""

sudo apt install python-celery-common
echo ""
echo "alternative install celery"
echo ""

