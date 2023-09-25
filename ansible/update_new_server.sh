#!/bin/bash
repo="ansible"
cd $repo
time ansible-playbook ansible/update_new_server.yml
