#!/bin/bash
repo="ansible"
cd $repo
# time ansible-playbook ansible/update_linux_server.yml
pwd
ls -l
time ansible-playbook update_linux_server.yml

