# 2 Junos packages PyEz and jxmlease 

pip install ansible
pip install junos-eznc
pip install jxmlease

# juniper.junos Ansible Galaxy role it's an app store for ansible
ansible-galaxy install Juniper.junos

# go to - cat /etc/ansible/hosts
# first devices managed by Ansible
vMX-1
vMX-2

[vmx-devices]
vMX-1
vMX-2

[vmx-devices:vars]
ntp_server = 172.25.11.254

