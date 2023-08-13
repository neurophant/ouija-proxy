Ouija Proxy
===========

Ouija TCP proxy server with UDP interface built on top of `Ouija <https://github.com/neurophant/ouija>`_ library

Features
--------

Hides TCP traffic in encrypted UDP traffic between relay and proxy servers

.. image:: https://raw.githubusercontent.com/neurophant/ouija-proxy/main/ouija.png
    :alt: UDP tunneling
    :width: 800

Setup - Ubuntu
--------------

.. code-block:: bash

    sudo apt install wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.11
    sudo apt-get install supervisor

    git clone https://github.com/neurophant/ouija-proxy.git
    cd ouija-proxy
    sudo cp conf/ouija-proxy.conf /etc/supervisor/conf.d/ouija-proxy.conf
    sudo cp conf/supervisord.conf /etc/supervisor/supervisord.conf
    sudo systemctl restart supervisor.service
