
# XPath Expressions to filter XML data.

from lxml import etree
import pprint

with open('./srx.interfaces.xml') as fh:
    interfaces_xml = etree.fromstring(fh.read())
    
def node_values_list(xml_doc, xpath_expr):
    return [ x.text for x in xml_doc.xpath(xpath_expr) ]

# Example Paths
xpath_all_nodes = '//name'    # starting '//' means find the subsequent path anywhere in the document
xpath_absolute = '/rpc-reply/interface-information/physical-interface/name'  # starting '/' means anchor at root

# Example Predicates:
xpath_starts_with = '/rpc-reply/interface-information/logical-interface[starts-with(name, "lo")]/name'
xpath_match = '/rpc-reply/interface-information/physical-interface[oper-status = "up"]/name'
xpath_not_match = '/rpc-reply/interface-information/physical-interface[oper-status != "up"]/name'
xpath_position = '/rpc-reply/interface-information/physical-interface[3]/name'
xpath_reverse_position = '/rpc-reply/interface-information/physical-interface[last()-1]/name'
