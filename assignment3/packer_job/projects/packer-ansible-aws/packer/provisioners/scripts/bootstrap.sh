#!/bin/bash
set -ex

# Add EPEL repository
sudo amazon-linux-extras install epel -y
sudo yum install  ansible -y
