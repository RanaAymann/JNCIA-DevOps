# !/usr/bin/python
from jnpr.junos import Device
from lxml import etree

if __name__ == '__main__':

    with Device(host="10.1.1.1", user="lab", password="lab123") as dev:
        cnf = dev.rpc.get_config(filter_xml=etree.XML(
            '<configuration><interfaces/></configuration>'))
        print(etree.tostring(cnf))

# use filter to retreive specific part in the configuration.
