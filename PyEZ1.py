# !/usr/bin/python
from jnpr.junos import Device

if __name__ == '__main__':

    with Device(host="10.1.1.1", user="lab", password="lab123") as dev:

        print(dev.facts)

# with will open and close the session.
