# Project Beer404 : Install

## Table Of Contents

- [Project Beer404 : Install](#project-beer404--install)
  - [Table Of Contents](#table-of-contents)
  - [Docker Install](#docker-install)
    - [Docker Linux](#docker-linux)
    - [Docker Windows](#docker-windows)
  - [Python and Pip Install](#python-and-pip-install)
    - [Python and Pip Windows](#python-and-pip-windows)
    - [Python and Pip Linux](#python-and-pip-linux)

## Docker Install

### Docker Linux

To install Docker on Linux, you can run these command :

    # Docker Uninstall
    echo "Docker Uninstall :"
    sudo apt-get remove -y \
      docker \
      docker-engine \
      docker.io \
      containerd \
      runc

    # Docker Install Dependencies
    echo "Docker Install Dependencies :"
    sudo apt-get install -y \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common

    sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

    sudo apt-key -y fingerprint 0EBFCD88

    sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/debian \
      $(lsb_release -cs) \
      stable"

    # Docker Install Engine
    echo "Docker Install Engine :"
    sudo apt-get update

    sudo apt-get install -y \
      docker-ce \
      docker-ce-cli \
      containerd.io

### Docker Windows

To install Docker on Windows, you can view this [guide](https://docs.docker.com/docker-for-windows/install/).

## Python and Pip Install

### Python and Pip Windows

Install Python with this [link](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64-webinstall.exe).

For Pip you have to download this Python script : [Get Pip](https://bootstrap.pypa.io/get-pip.py)

Next you will install Pip with this command :

    Open CMD in the folder where is get-pip.py !

    python get-pip.py

Finish you have got Pip !

### Python and Pip Linux

    # Python Install
    echo "Python Install :"
    sudo apt-get install -y \
      python-pip \
      python-setuptools \
      python3 \
      python3-dev \
      python3-pip \
      python3-setuptools \
      python3-venv && \
      if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi

    # Pip Install
    echo "Pip Install :"
    pip3 install --no-cache --upgrade \
      pip \
      setuptools \
      wheel && \
      if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
