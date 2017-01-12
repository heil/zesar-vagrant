
import sys

from lxml import etree, objectify
from lxml.etree import XMLSchema

xml_file = sys.argv[1]
schema_file = sys.argv[2]

xsd_string = file(schema_file, 'rb').read()
xmlschema = XMLSchema(etree.fromstring(xsd_string))

content_xml = file(xml_file, 'rb').read().strip()

parser = objectify.makeparser(schema=xmlschema)
try:
    validated_document = objectify.fromstring(content_xml, parser=parser)
except etree.XMLSyntaxError as e:
    print "invalid: %r" % e
else:
    print 'valid'
