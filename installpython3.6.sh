#!/usr/bin/env bash

echo 'disable firewalld'
sleep 3
systemctl stop firewalld
systemctl disable firewalld

yum install -y epel-release; yum install -y python36 python36-devel python36-setuptools

chmod -R +x /root/domain/*.py

echo "Enter hostname: "
read server

echo $server > /etc/hostname

echo 'install done!!! and reboot after 5s'

sleep 5

reboot now
