cd /home/ec2-user/projects/packer-ansible-aws/packer
packer build -machine-readable packer-build.json | tee build_artifact.txt


cd 
source .bashrc
sudo ansible-playbook -i /etc/ansible/projects/hosts /etc/ansible/projects/main.yml --extra-vars "image_id=$id" -vvv

