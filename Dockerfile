### 1. Get Linux
FROM ubuntu:focal

### 2. Get Java via the package manager
RUN apt update
### 3. Get Python, PIP

RUN apt-get -y install software-properties-common openjdk-8-jdk\
    && add-apt-repository --yes --update ppa:deadsnakes/ppa \
    && apt-get -y install python3.6\
    && useradd -rm -d /home/ipdr -u 1001 ipdr
    # && useradd -rm -d /home/ipdr -s /bin/bash -g root -G sudo -u 1001 ipdr