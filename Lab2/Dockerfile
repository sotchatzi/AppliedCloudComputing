FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update 
RUN apt-get -y upgrade 
RUN apt-get install -y git 
#RUN apt-get install -y software-properties-common
#RUN add-apt-repository universe
#RUN apt-get update 
#RUN apt-get install -y python
#RUN apt-get update 
#RUN apt-get install -y software-properties-common && add-apt-repository universe 
#RUN apt-get update 
RUN apt-get install -y python3-pip
#RUN pip3 install --upgrade pip3
RUN pip3 install flask
RUN apt-get install -y cowsay
RUN git clone https://github.com/TDB-UU/csaas.git 
WORKDIR /csaas/cowsay
EXPOSE 5000
ENV PATH="${PATH}:/usr/games/"
CMD ["python3","app.py"]
