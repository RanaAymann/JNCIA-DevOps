# !/usr/bin/python
from jnpr.junos import Device

if __name__ == '__main__':

    dev = Device(host="10.1.1.1", user="lab", password="lab123")
    dev.open()
    print(dev.facts)
    dev.close()

# collect junos facts
