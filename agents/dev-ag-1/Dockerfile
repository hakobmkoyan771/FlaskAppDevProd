FROM jenkins/ssh-agent:jdk11

USER 0

RUN apt-get -y install python && \
    apt-get -y install python3-pip

RUN pip3 install pytest
