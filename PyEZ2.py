# !/usr/bin/python
from jnpr.junos import Device

if __name__ == '__main__':

    dev = Device(host="10.1.1.1", user="lab", password="lab123")
    dev.open()
    route_lxml_element = dev.rpc.get_route_information(table="inet.0")
    list_of_routes = route_lxml_element.findall('.//rt')
    for route in list_of_routes:
        print("Route: {} Protocol: {} ".format(route.findtext('rt-destination').strip(),
                                               route.findtext('rt-entry/protocol-name').strip()))

    dev.close()

# get route information for inet 0
# rpc call available in python
# rpc call returns an lxml element object that may be parsed using XPath.
