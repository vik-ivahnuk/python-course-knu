from lxml import etree, objectify
from lxml.etree import XMLSyntaxError

def validate_xml(xml_path: str, xsd_path: str)->bool:
    try:
        schema = etree.XMLSchema(file=xsd_path)
        parser = objectify.makeparser(schema=schema)
        objectify.parse(xml_path, parser)
    except XMLSyntaxError as e:
        print("Error  ", e)
        return False
    return True


